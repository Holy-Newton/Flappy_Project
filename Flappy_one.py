import pygame
import math as m
from pynput import keyboard

pygame.init()

WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("HOLLY_HOLLY_HOLLY_HOLLY------ FLAPPY-BIRD by Holly-Newton -----HOLLY_HOLLY_HOLLY_HOLLY")

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
GRAVITY = 8
TIME_STEP = 1
y = HEIGHT/2
Vy = 0
#-----------------------PICTURES---------------------------------

bird_image = pygame.image.load('BIRD.png')
tube_image = pygame.image.load('TUBE.png')

bird_image = pygame.transform.scale(bird_image, (90,90))
tube_image_fliped = pygame.transform.flip(tube_image, False, True)

#----------------------BIRD_MOVMEMENT----------------------------      
            

#-----------------------------------------------------------------
def init():
    global y
    global Vy
    run = True
    clock = pygame.time.Clock()

    
    JUMP = False

    while run:
        clock.tick(60)
        WIN.fill(BLUE_SKY)


        
        #------------------EVENTS-------------------------
        
    
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    JUMP = True

        if JUMP:
            Vy = -10
        else:
            Vy = Vy
        JUMP = False
        y = y + Vy + GRAVITY
        WIN.blit(bird_image, ((WIDTH/2-200),y))
        WIN.blit(tube_image, ((WIDTH/2), HEIGHT/2))
        WIN.blit(tube_image_fliped, ((WIDTH/2), 0))  
        pygame.display.update()
    pygame.quit()


init()






















