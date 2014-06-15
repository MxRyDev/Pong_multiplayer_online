
# Import 3rd party Libraries:
import pygame
from pygame.locals import *
import random

# import custom libries
from constants import *
from player_class import *
from puck_class import *

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# Init pygame stuff:
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong LOCAL (Pre-alpha)')
screen = pygame.display.set_mode(SCREEN_SIZE)

# --- create game objects ---
player_1 = Player(SCREEN_WIDTH - (50+PLAYER_WIDTH), player2_image) 
player_2 = Player(50, player1_image)
puck = Puck()









#`````````````````````````````````````````````````````````````````````````````````#
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

