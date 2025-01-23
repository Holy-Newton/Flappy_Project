import pygame
import os
import math as m
from pynput import keyboard

pygame.init()

WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("------Flappy-Bird-------- by Holly_Newton")

#------------------------COLORS----------------------------------

WHITE = (240, 240, 240)
VENUS_YELLOW = (237, 201, 175)
YELLOW = (255, 255, 0)
BLUE = (34, 139, 230)
RED = (201, 52, 37)
DARK_GREY = (169, 169, 169)
SATURN_COLOR = (210, 180, 140)
JUPITER_COLOR = (200, 100, 50)
SPACE_GREY_BLUE = (10, 12, 40)


BLUE_SKY = (140, 190, 255)
GROUND = (222, 186, 136)
GRASS = (141, 228, 69)
TUBE = (98, 203, 60)
YELLOW_BIRD = (255, 254, 70)
ORANGE_BIRD = (255, 180, 45)
WHITE_WING = (255, 230, 200)


#----------------------PARAMETERS--------------------------------

SPEED = 10
GRAVITY = -10
JUMP = 10


#-----------------------PICTURES---------------------------------

bird_image = pygame.image.load('BIRD.png')
tube_image = pygame.image.load('TUBE.png')

bird_image = pygame.transform.scale(bird_image, (90,90))
tube_image_fliped = pygame.transform.flip(tube_image, False, True)
#------------------------MOVES----------------------------------


class move:
    def __init__(self, x, y, Vx, Vy, Ay, image):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Ay = Ay
        self.image = image
    
    def jump(self):
            if self == bird:
                self.Vy = JUMP
            
    def position_update(self):
        self.x += self.Vx
        if self == bird:
            self.y += self.Vy + GRAVITY/2
        self.y += self.Vy
        
            
    

def init():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        WIN.fill(BLUE_SKY)
        
        #-----------------OBJECTS-------------------------
        bird = move(WIDTH/2-200, HEIGHT/2 + 20, 0, 0 ,GRAVITY, bird_image)
        tube_up = move(WIDTH-50, HEIGHT/2 + 20, SPEED, 0 ,0, tube_image)
        tube_down = move(WIDTH-50, 0, SPEED, 0 ,0, tube_image_fliped)
      
        

        Object = [bird, tube_up, tube_down]



        #------------------EVENTS-------------------------
        
        for move in Object:
                move.position_update()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move.Jump(bird)
            

                
        #WIN.blit(bird_image, ((WIDTH/2-200), HEIGHT/2))
        #WIN.blit(Tube_image, ((WIDTH/2), HEIGHT/2))
        #WIN.blit(Tube_image_fliped, ((WIDTH/2), 0))  
        pygame.display.update()
    pygame.quit()


init()






















