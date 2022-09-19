import pygame 
pygame.init()
Ancho =700
Alto = 500
Pantalla = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Proyecto Final")

#Parametros
fps = 60
blanco = (255, 255, 255)
negro = (0, 0, 0)

#Clases
class Paleta:
  

    def __init__(self, x, y, width, height,color):
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
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y

class Bola:
    Vel = 5

    def __init__(self, x, y, radio,color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radio = radio
        self.x_vel = self.Vel
        self.y_vel = 0
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def mover(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reseteo(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1