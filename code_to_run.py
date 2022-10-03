
from betterpong import pygame, Paleta,Bola,Jugar
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

    Puntaje_Izq = 0
    Puntaje_Der = 0

    while run:
        clock.tick(fps)
        draw(Pantalla, [P_Izq, P_Der], bola, Puntaje_Izq, Puntaje_Der)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        Jugar.moverPaleta(keys, P_Izq, P_Der)

        bola.mover()
        Jugar.choque(bola, P_Izq, P_Der)
        
        

    pygame.quit()


if __name__ == '__main__':
    main()