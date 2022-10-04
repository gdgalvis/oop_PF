import pygame
fps = 60
blanco = (255, 255, 255)
negro = (0, 0, 0)
Paltura=100
Pancho=20
Bradio=7
Ancho =700
Alto = 500
#Clases
class Paleta:
    vel=4
    def __init__(self, x, y, width, height,color=(255, 255, 255)):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def mover(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y

class Bola:
    Vel = 5
    def __init__(self, x, y, radio,color=(255, 255, 255)):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radio = radio
        self.x_vel = self.Vel
        self.y_vel = 0
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)

    def mover(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

class Jugar:
    def choque(ball, P_Izq, P_Der, P_Izq1, P_Der1,P_Izq2, P_Der2):
        if ball.y + ball.radio >= Alto:
            ball.y_vel *= -1
        elif ball.y - ball.radio <= 0:
            ball.y_vel *= -1
        
        if ball.x + ball.radio >= Ancho:
            ball.x_vel *= -1
        elif ball.x - ball.radio <= 0:
            ball.x_vel *= -1

        if ball.x_vel < 0:
            if ball.y >= P_Izq.y and ball.y <= P_Izq.y + P_Izq.height:
                if ball.x - ball.radio <= P_Izq.x + P_Izq.width:
                    ball.x_vel *= -1

                    middle_y = P_Izq.y + P_Izq.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (P_Izq.height / 2) / ball.Vel
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

        else:
            if ball.y >= P_Der.y and ball.y <= P_Der.y + P_Der.height:
                if ball.x + ball.radio >= P_Der.x:
                    ball.x_vel *= -1

                    middle_y = P_Der.y + P_Der.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (P_Der.height / 2) / ball.Vel
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel


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
    

    def music(song):
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)

    def Puntaje(bola, P_Izq, P_Der,Puntaje_Izq,Puntaje_Der,Pantalla,Letra):
        pass