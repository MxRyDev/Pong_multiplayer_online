if __name__ == '__main__':
    print('''
    This file is used to define the CONSTANTS for Local Pong.
    it is to be used within "MAIN.py".
    on its own, it provides no functionality.
    
    HAFF A GUD DAY
    ''')
    
import pygame

screen = pygame.display.set_mode([10,10])


# lists:
all_sprites_list = pygame.sprite.Group()
player_list      = pygame.sprite.Group()
puck_list        = pygame.sprite.Group()

# colors:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
    
# ------- 'tweakable' consants -------
    
# screen setup
SCREEN_WIDTH = 1199  #width and height match bg image below
SCREEN_HEIGHT = 700
SCREEN_SIZE = ([SCREEN_WIDTH, SCREEN_HEIGHT])
    

# game elements:
# these are based on bitmapped image size
# they should be updated if images are changed
PLAYER_HEIGHT = 200 
PLAYER_WIDTH = 50
PLAYER_SPEED = 15

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