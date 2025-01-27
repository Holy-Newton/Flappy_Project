import pygame
import math as m
from pynput import keyboard
import random
pygame.init()

WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("HOLY_HOLY_HOLY_HOLY_HOLY_HOLY_HOLY------ FLAPPY-BIRD by Holy-Newton -----HOLY_HOLY_HOLY_HOLY_HOLY_HOLY_HOLY")

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

FONT_TITLE = pygame.font.SysFont("marker felt",40)
FONT_TITLE_POINT = pygame.font.SysFont("marker felt",80)

BLUE_SKY = (140, 190, 255)
GROUND = (222, 186, 136)
GRASS = (141, 228, 69)
TUBE = (98, 203, 60)
YELLOW_BIRD = (255, 254, 70)
ORANGE_BIRD = (255, 180, 45)
WHITE_WING = (255, 230, 200)


#----------------------PARAMETERS--------------------------------
FLY = 10.5
SPEED = 10
GRAVITY = 0.8
TIME_STEP = 1
y = HEIGHT/2
Vy = 0
Tx = WIDTH
T2x = WIDTH
alea = 2
alea2 = 3
decount = 70
point = 0
#-----------------------PICTURES---------------------------------
cloud_image = pygame.image.load('CLOUD.png')
bird_image = pygame.image.load('BIRD.png')
tube_image = pygame.image.load('TUBE.png')

bird_image = pygame.transform.scale(bird_image, (70,50))
tube_image = pygame.transform.scale(tube_image, (120,600))
tube_image_fliped = pygame.transform.flip(tube_image, False, True)
tube_image2 = tube_image
tube_image_fliped2 = tube_image_fliped


#-------------------------MOVMEMENTS------------------------------    
            
            
def Tube_mv(Tx, H):
    WIN.blit(tube_image_fliped, (Tx, 50-H*60))
    WIN.blit(tube_image, (Tx, WIDTH/1.5-H*60))
    
def Tube2_mv(Tx, H):
    WIN.blit(tube_image_fliped2, (Tx, 50-H*60))
    WIN.blit(tube_image2, (Tx, WIDTH/1.5-H*60))

def collide(a,b,c):
    if b.colliderect(a):
        return True
    if c.colliderect(a):
        return True
    else:
        return False








#-------------------------INITIALISATION--------------------------
def init():
    global y
    global Vy
    global Tx
    global T2x
    global alea
    global alea2
    global decount
    global point
    run = True
    clock = pygame.time.Clock()
    
    
    JUMP = False
    Collision = False





    while run:
        clock.tick(60)
        WIN.fill(BLUE_SKY)
        WIN.blit(cloud_image, (9,0))
        Intern_title=FONT_TITLE.render("FLAPPY BIRD by Holy_Newton", 1, YELLOW_BIRD)
        WIN.blit((Intern_title), (100,100)) 
        #---------COLLISION STUFF:--------------------------

        rect_bird = bird_image.get_rect(topleft=(WIDTH/2-200,y))
        
        rect_tube = tube_image.get_rect(topleft=(Tx, WIDTH/1.5-alea*60))
        rect_tube_fliped = tube_image_fliped.get_rect(topleft=(Tx, 50-alea*60))
        Collision = collide(rect_bird ,rect_tube ,rect_tube_fliped)
        if Collision:
            run = False
            print(f"{point} collision !!!")

        if decount<0:
            rect_tube2 = tube_image2.get_rect(topleft=(T2x, 50-alea2*60))
            rect_tube_fliped2 = tube_image_fliped2.get_rect(topleft=(T2x, 50-alea2*60))
            Collision = collide(rect_bird ,rect_tube2 ,rect_tube_fliped2)

        
        
        if Collision:
            run = False
            print(f"{point} collision !!!")


        #------------------EVENTS-------------------------
        if Tx == WIDTH/2-200:
            point += 1
        if T2x == WIDTH/2-200:
            point += 1
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    JUMP = True
                   

        ##BIRD MANIPULATION ###
        if JUMP:
            Vy = -FLY
        else:
            Vy = Vy+ GRAVITY
        JUMP = False
        y = y + Vy

        if y > HEIGHT - bird_image.get_height():
            y = HEIGHT - bird_image.get_height()
        elif y < 0:
            y = 0

        WIN.blit(bird_image, ((WIDTH/2-200),y))

        ### TUBE MANIPULATION ###

        Tx += -SPEED
        if Tx > -100:
            Tube_mv(Tx,alea)
        else:
            alea = random.randint(1,9)
            Tx = WIDTH+100

        if decount<0:
            T2x += -SPEED
            if T2x > -100:
                Tube2_mv(T2x,alea2)
            else:
                alea2 = random.randint(1,9)
                T2x = WIDTH+100

        decount -= 1

        POINT=FONT_TITLE_POINT.render(f"{point}", 1, WHITE)
        WIN.blit((POINT), (WIDTH - 150,100))

        pygame.display.update()

    pygame.quit()

    
    
init()



















