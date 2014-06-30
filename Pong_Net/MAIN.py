# Need to add:
'''

-Scoring

'''


# Import 3rd party Libraries:
import pygame
from pygame.locals import *
import random, sys


# Import custom libraries:
from constants import *
from player_class import *
from puck_class import *
from event_handling import *
from remote_player_class import *

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# Init pygame stuff:
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Pong LOCAL (Pre-alpha)')
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.toggle_fullscreen()
font = pygame.font.Font(None, 90)

# --- create game objects ---
player_1 = Player(SCREEN_WIDTH - (50+PLAYER_WIDTH), player2_image)
p_list.append(player_1)
player_2 = Player(50, player1_image)
p_list.append(player_2)
puck = Puck(p_list)

remote_player = Remote_player()



# ---create event exe's---

# create list that all actions will be added to
al = []   # this will let the Event_conductor iterate through the actions


# creates actions. passed arguments are:
# KEY, method/function for keyup, method/function for keydown, actions list
p1_up       = Event_exe(K_UP, player_1.move_up, player_1.move_down, al)
p1_down     = Event_exe(K_DOWN, player_1.move_down, player_1.move_up, al)
p2_up       = Event_exe(K_w, player_2.move_up, player_2.move_down, al)
p2_down     = Event_exe(K_s, player_2.move_down, player_2.move_up, al)
puck_reset  = Event_exe(K_F2, puck.reset, ignore, al)

# create event conductor object, pass it the list of actions we want:
event_conductor = Event_conductor(al)



#`````````````````````````````````````````````````````````````````````````````````#
# _________________________----- Main Loop -----_________________________________ #
done = False

# --- event handling ---
while not done:
    while True:
        if remote_player.x == 'go':
            break
    
    # --- handle events ---
    event_conductor.handle_events(pygame.event.get(), pygame.mouse.get_pressed())
    

    # --- move objects ---
    for object in all_sprites_list:
        object.move()
    
    
    
    # --- draw objects ---

    # blits bg image:
    screen.blit(background_image, background_position)
    
    # updates/draws sprites
    all_sprites_list.update()
    remote_player.speak(player_1.rect.x, player_1.rect.y)
    player_2.rect.y = remote_player.y
    
    
    all_sprites_list.draw(screen)
    
    # draws score:
    p1_score = font.render(str(player_1.score), 1, (GREEN))
    p2_score = font.render(str(player_2.score), 1, (BLUE))
    screen.blit(p1_score, (SCREEN_WIDTH - (SCORE_PAD + 35), 0))
    screen.blit(p2_score, (SCORE_PAD, 0))
    

    # flips the display:
    pygame.display.flip()

    # limits framerate:
    clock.tick(60)
    
#closes game:
pygame.quit()
sys.exit()