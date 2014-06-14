
# Import Libraries:
import pygame
from pygame.locals import *
import random
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# Init pygame stuff:
pygame.init()
clock = pygame.time.Clock()


# screen setup
SCREEN_WIDTH = 1199  #width and height match bg image below
SCREEN_HEIGHT = 700
SCREEN_SIZE = ([SCREEN_WIDTH, SCREEN_HEIGHT])
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pong LOCAL (Pre-alpha)')



# --- constants ---

# colors:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# game elements:
PLAYER_HEIGHT = 200 #these need to be based on bitmapped image size
PLAYER_WIDTH = 50
PLAYER_SPEED = 10

PUCK_HEIGHT = 30
PUCK_WIDTH = 30
PUCK_SPEED = 7





# --- import files ---

#IMAGES:
background_image = pygame.image.load("hockey-ice-background.jpg").convert()
#(1199x740 pi)
background_position = [0,0]

player1_image =    pygame.image.load("blue_paddle.png").convert()
#(50x200 pi)

player2_image =    pygame.image.load("green_paddle.png").convert()
#(50x200 pi)

puck_image =       pygame.image.load("black_ball.png").convert()
#(30x30 pi ball)

# Makes the white background transparent on image
puck_image.set_colorkey(WHITE)

    
#________________________________________________________________________________#
#--------------------------------------------------------------------------------#
#````````````````````````````````````````````````````````````````````````````````#

# --- create sprite lists ---
all_sprites_list = pygame.sprite.Group()
player_list      = pygame.sprite.Group()
puck_list        = pygame.sprite.Group()


# --- create classes ---


# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    
    def __init__(self, startx, image):
        # init position variables
        self.change_x = 0
        self.change_y = 0
        # inherited class init
        pygame.sprite.Sprite.__init__(self)
        
        # setup image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = (SCREEN_HEIGHT/2 - PLAYER_HEIGHT/2)
        
        # add to lists
        all_sprites_list.add(self)
        player_list.add(self)
        
    # Define movement methods:
    def changespeed(self, y):
        self.change_y += y
        
    def move(self):
        
        # move
        self.rect.y += self.change_y
        
        # keep on screen:
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
            
# PUCK CLASS
class Puck(pygame.sprite.Sprite):
    def __init__(self):
        # init position variables
        self.choices = [PUCK_SPEED, -1*PUCK_SPEED]
        self.change_x = random.choice(self.choices)
        self.change_y = random.randint(-1*PUCK_SPEED, PUCK_SPEED)
        # inherited class init
        pygame.sprite.Sprite.__init__(self)
        
        #setup image
        self.image = puck_image
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH/2 - PUCK_WIDTH/2)
        self.rect.y = (SCREEN_HEIGHT/2 - PUCK_HEIGHT/2)
        
        # add to lists
        all_sprites_list.add(self)
        puck_list.add(self)
        
    # Define movement methods:
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    def move(self):
        
        # move
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        # bounce off of top/bottom of screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.change_y *= -1
        elif self.rect.top < 0:
            self.change_y *= -1
    

    
# --- create game objects ---
player_1 = Player(SCREEN_WIDTH - (50+PLAYER_WIDTH), player2_image) 
player_2 = Player(50, player1_image)
puck = Puck()

# _________________________----- Main Loop -----_________________________________ #
done = False

# --- event handling ---
while not done:
    
    # Get all the events
    for event in pygame.event.get():
        
        # handle 'quit'
        if event.type == pygame.QUIT:
            done = True
            
        #handle pressed keys:
        elif event.type == pygame.KEYDOWN:
            
            #(right player [p1])
            if event.key == pygame.K_UP:
                player_1.changespeed(-1*PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(PLAYER_SPEED)
                
            #(left player [p2])
            elif event.key == pygame.K_w:
                player_2.changespeed(-1*PLAYER_SPEED)
            elif event.key == pygame.K_s:
                player_2.changespeed(PLAYER_SPEED)
                
            #FOR DEV ONLY:
            elif event.key == pygame.K_F2:
                puck.remove()
                all_sprites_list.remove(puck)
                
                puck = Puck()
                
                
                
        # handle released keys:
        elif event.type == pygame.KEYUP:
            #(right player [p1])
            if event.key == pygame.K_UP:
                player_1.changespeed(PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(-1*PLAYER_SPEED)
            #(left player [p2])
            elif event.key == pygame.K_w:
                player_2.changespeed(PLAYER_SPEED)
            elif event.key == pygame.K_s:
                player_2.changespeed(-1*PLAYER_SPEED)
            
            
#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#


    # --- move objects ---
    for object in all_sprites_list:
        object.move()
    
    
    
    # --- draw objects ---

    # blits bg image:
    screen.blit(background_image, background_position)
    
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    

    # flips the display:
    pygame.display.flip()

    # limits framerate:
    clock.tick(60)
    
#closes game:
pygame.quit()

