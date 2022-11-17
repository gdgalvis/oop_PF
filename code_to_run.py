#This file is part of betterpong.

#Betterpong is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#Betterpong is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with Betterpong. If not, see <https://www.gnu.org/licenses/>.
#«Copyright 2022 Galvis German, Tornet Diego»

from betterpong import pygame, Paleta,Bola,Jugar
from pygame.locals import *
from pygame import mixer 
pygame.init()
Ancho =700
Alto = 500
Pantalla = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Proyecto Final")

#Parametros
fps = 60
blanco = (255, 255, 255)
negro = (0, 0, 0)
Paltura=100
Pancho=20
Bradio=7

Letra = pygame.font.SysFont("comicsans", 50)
ganar = 10

def draw(win, paddles, ball, left_score, right_score):
    win.fill(negro)

    left_score_text = Letra.render(f"{left_score}", 1, blanco)
    right_score_text = Letra.render(f"{right_score}", 1, blanco)
    win.blit(left_score_text, (Ancho//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (Ancho * (3/4) -
                                right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)

    ball.draw(win)
    pygame.display.update()





def main():
    run = True
    clock = pygame.time.Clock()

    P_Izq = Paleta(10, Alto//2 - Paltura//2, Pancho, Paltura)
    P_Der = Paleta(Ancho - 10 - Pancho, Alto //2 - Paltura//2, Pancho, Paltura)
    bola = Bola(Ancho // 2, Alto // 2, Bradio)

    #Paletas Secundarias
    P_Izq1 = Paleta(225, Paltura//2, Pancho, Paltura//2)
    P_Izq2 = Paleta(225, Alto- Paltura, Pancho, Paltura//2)
    P_Der1 = Paleta(Ancho - 225 - Pancho, Paltura//2, Pancho, Paltura/2)
    P_Der2 = Paleta(Ancho - 225 - Pancho, Alto- Paltura, Pancho, Paltura/2)


    Puntaje_Izq = 0
    Puntaje_Der = 0

    Jugar.music("BG1.wav")
    while run:
        clock.tick(fps)
        draw(Pantalla, [P_Izq, P_Der,P_Izq1, P_Der1,P_Izq2, P_Der2], bola, Puntaje_Izq, Puntaje_Der)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        Jugar.moverPaleta(keys, P_Izq, P_Der,P_Izq1, P_Der1,P_Izq2, P_Der2)

        bola.mover()
        Jugar.choque(bola, P_Izq, P_Der,P_Izq1, P_Der1,P_Izq2, P_Der2)
        if bola.x + bola.radio< 0:
            Puntaje_Der += 1
            bola.reseteo()
        elif bola.x + bola.radio > Ancho:
            Puntaje_Izq += 1
            bola.reseteo()

        ganar=10
        won = False
        if Puntaje_Izq >= ganar:
            won = True
            win_text = "GANO JUGADOR IZQ!"
        elif Puntaje_Der >= ganar:
            won = True
            win_text = "GANO JUGADOR DER"

        if won:
            text = Letra.render(win_text, 1, blanco)
            Pantalla.blit(text, (Ancho//2 - text.get_width() //
                            2, Alto//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            bola.reseteo()
            P_Izq.reseteo()
            P_Der.reseteo()
            Puntaje_Izq = 0
            Puntaje_Der = 0

    pygame.quit()


if __name__ == '__main__':
    main()
