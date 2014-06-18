
# Import 3rd party Libraries:
import pygame
from pygame.locals import *
import random, sys

# import custom libries
from constants import *
from player_class import *
from puck_class import *
from event_handling import *

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

# ---create event exe's---
actions_list = []

p1_move_up = Event_exe(pygame.K_UP, 
                       player_1.changespeed(PLAYER_SPEED), 
                       player_1.changespeed(-PLAYER_SPEED),
                       actions_list
                       )

p1_move_down = Event_exe(pygame.K_DOWN, 
                         player_1.changespeed(-PLAYER_SPEED),
                         player_1.changespeed(PLAYER_SPEED),
                         actions_list
                         )

p2_move_up = Event_exe(pygame.K_w,
                       player_2.changespeed(PLAYER_SPEED),
                       player_2.changespeed(-PLAYER_SPEED),
                       actions_list
                       )

p2_move_down =  Event_exe(pygame.K_s,
                          player_2.changespeed(-PLAYER_SPEED),
                          player_2.changespeed(PLAYER_SPEED),
                          actions_list
                          )

# create event conductor object, pass it the list of actions we want:
event_conductor = Event_conductor(actions_list)
print(actions_list)



#`````````````````````````````````````````````````````````````````````````````````#
# _________________________----- Main Loop -----_________________________________ #

done = False

# --- event handling ---
while not done:
    
    event_conductor.handle_events(pygame.event.get())
    


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
sys.exit()
