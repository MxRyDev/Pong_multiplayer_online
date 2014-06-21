# Defines the puck class to be imported into pong/MAIN

if __name__ == '__main__':
    print('''
    This file is used to define the PUCK class for Local Pong.
    it is to be used within "localpong_main.py".
    on its own, it provides no functionality.
    
    HAFF A GUD DAY
    ''')
    
import pygame.sprite
from random import randint, choice
from constants import *


    
# PUCK CLASS
class Puck(pygame.sprite.Sprite):
    
    
    def __init__(self, list):
        
        self.p_list = list
        self.passed = False
        # init position variables
        self.choices = [PUCK_SPEED, -1*PUCK_SPEED]
        self.change_x = choice(self.choices)
        self.change_y = choice(self.choices)
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
        
    def reset(self):
        self.rect.x = (SCREEN_WIDTH/2 - PUCK_WIDTH/2)
        self.rect.y = (SCREEN_HEIGHT/2 - PUCK_HEIGHT/2)
        self.change_x = choice(self.choices)
        self.change_y = randint(-1*PUCK_SPEED, PUCK_SPEED)
        print('reset')
    
    def reverse_x(self, buff = 0):
        self.change_x *= -1
        self.rect.x += buff
        self.passed = False
        
    def reverse_y(self, buff = 0):
        self.change_y *= -1
        self.rect.y += buff
        self.passed = False
  
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
            
        # reset when travels off screen on x axis
        # (update this when scoring & better reset are implemented)
        if self.rect.x <-600 or self.rect.x>(SCREEN_WIDTH+600):
            self.reset()
            
            
        # Collision check:
        puck_hit_player = pygame.sprite.spritecollide(self, player_list, False)
        
        if puck_hit_player:
            # check
            for player in puck_hit_player:
                if self.passed:
                    self.reverse_y()
                
                else:
                    if player.rect.x > SCREEN_WIDTH/2:
                        pad = player.rect.left - self.rect.right
                    else:
                        pad = player.rect.right - self.rect.left
                    self.reverse_x(pad)
                    print(pad)
                    
                # add spin:
                if player.change_y > 0:
                    if self.change_y > 0:
                        self.change_y += SPIN_SPEED
                        self.change_x += SPIN_SPEED/2
                    elif self.change_y < 0:
                        self.change_y -= DRAG_SPEED
                        self.change_y -= DRAG_SPEED/2
                if player.change_y < 0:
                    if self.change_y < 0:
                        self.change_y -= SPIN_SPEED
                        self.change_x -= SPIN_SPEED/2
                    elif self.change_y > 0:
                        self.change_y += DRAG_SPEED
                        self.change_y += DRAG_SPEED/2
                
                if self.change_y < PUCK_SPEED:
                    self.change_y = PUCK_SPEED
                if self.change_x < PUCK_SPEED:
                    self.change_x = PUCK_SPEED
                    
                    
        # check to see if puck will 
        # bounce of top/bottom of player
        # only runs if no collides
        else:
            # if puck is going right:
            if self.change_x > 0:
                # see if passed right player:
                if self.rect.right >= p_list[0].rect.left:
                    self.passed = True
            # same if puck is going left:
            elif self.change_x < 0:
                if self.rect.left <= p_list[1].rect.right:
                    self.passed = True
            else: self.passed = False