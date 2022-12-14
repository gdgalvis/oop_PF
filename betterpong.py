#This file is part of betterpong.

#Betterpong is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#Betterpong is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with Betterpong. If not, see <https://www.gnu.org/licenses/>.
#«Copyright 2022 Diego Tornet, German Galvis»

import pygame

Alto = 500
#Clases

#Crea la paletas
class Paleta:
    vel=4
    def __init__(self, x, y, width, height,color=(255, 255, 255)):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color
    
    #Dibuja las paletas
    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
    
    def mover(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel
   
    #Reinicia las paletas
    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y

#Se crea la bola
class Bola:
    Vel = 5
    def __init__(self, x, y, radio,color=(255, 255, 255)):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radio = radio
        self.x_vel = self.Vel
        self.y_vel = 0
        self.color = color
    
    #Dibuja la bola
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)

    def mover(self):
        self.x += self.x_vel
        self.y += self.y_vel

    #Reinicia la bola
    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
#La clase que contiene juego
class Jugar:
    def choque(bola, P_Izq, P_Der, P_Izq1, P_Der1,P_Izq2, P_Der2):

        #Maneja las colisiones con paredes
        if bola.y + bola.radio >= Alto:
            bola.y_vel *= -1
        elif bola.y - bola.radio <= 0:
            bola.y_vel *= -1
        

        #Maneja las colisiones con paletas
        if bola.x_vel < 0:
            #Maneja las colisiones con Paleta Principal Izquierda
            if bola.y >= P_Izq.y and bola.y <= P_Izq.y + P_Izq.height:
                if bola.x - bola.radio <= P_Izq.x + P_Izq.width:
                    bola.x_vel *= -1

                    middle_y = P_Izq.y + P_Izq.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Izq.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel
                    
            #Maneja las colisiones con Paleta Secundaria 1 Izquierda
            if bola.y >= P_Izq1.y and bola.y <= P_Izq1.y + P_Izq1.height:
                if bola.x - bola.radio <= P_Izq1.x + P_Izq1.width:
                    bola.x_vel *= -1

                    middle_y = P_Izq1.y + P_Izq1.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Izq1.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel

            #Maneja las colisiones con Paleta Secundaria 2 Izquierda
            if bola.y >= P_Izq2.y and bola.y <= P_Izq2.y + P_Izq2.height:
                if bola.x - bola.radio <= P_Izq2.x + P_Izq2.width:
                    bola.x_vel *= -1

                    middle_y = P_Izq2.y + P_Izq2.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Izq2.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel


        else:
            #Maneja las colisiones con Paleta Principal Derecha
            if bola.y >= P_Der.y and bola.y <= P_Der.y + P_Der.height:
                if bola.x + bola.radio >= P_Der.x:
                    bola.x_vel *= -1
                    middle_y = P_Der.y + P_Der.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Der.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel

            #Maneja las colisiones con Paleta Secundaria 1 Derecha
            if bola.y >= P_Der1.y and bola.y <= P_Der1.y + P_Der1.height:
                if bola.x + bola.radio >= P_Der1.x:
                    bola.x_vel *= -1
                    middle_y = P_Der1.y + P_Der1.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Der1.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel

            #Maneja las colisiones con Paleta Secundaria 2 Derecha
            if bola.y >= P_Der2.y and bola.y <= P_Der2.y + P_Der2.height:
                if bola.x + bola.radio >= P_Der2.x:
                    bola.x_vel *= -1
                    middle_y = P_Der2.y + P_Der2.height / 2
                    difference_in_y = middle_y - bola.y
                    reduction_factor = (P_Der2.height / 2) / bola.Vel
                    y_vel = difference_in_y / reduction_factor
                    bola.y_vel = -1 * y_vel

    #Mueve las paletas
    def moverPaleta(keys, P_Izq, P_Der,P_Izq1, P_Der1,P_Izq2, P_Der2):
        #Lado Izquierda
        if keys[pygame.K_w] and P_Izq.y - P_Izq.vel >= 0:
            P_Izq.mover(up=True)
        if keys[pygame.K_s] and P_Izq.y + P_Izq.vel + P_Izq.height <= Alto:
            P_Izq.mover(up=False)
        if keys[pygame.K_a] and P_Izq1.y - P_Izq1.vel >= 0:
            P_Izq1.mover(up=True)
            P_Izq2.mover(up=True)
        if keys[pygame.K_d] and P_Izq2.y + P_Izq2.vel + P_Izq2.height <= Alto:
            P_Izq1.mover(up=False)
            P_Izq2.mover(up=False)

        #Lado Derecho
        if keys[pygame.K_UP] and P_Der.y - P_Der.vel >= 0:
            P_Der.mover(up=True)
        if keys[pygame.K_DOWN] and P_Der.y + P_Der.vel + P_Der.height <= Alto:
            P_Der.mover(up=False)
        if keys[pygame.K_LEFT] and P_Der1.y - P_Der1.vel >= 0:
            P_Der1.mover(up=True)
            P_Der2.mover(up=True)
        if keys[pygame.K_RIGHT] and P_Der2.y + P_Der2.vel + P_Der2.height <= Alto:
            P_Der1.mover(up=False)
            P_Der2.mover(up=False)
    
    #Musica del juego
    def music(song):
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)
