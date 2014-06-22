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
    
  
    # Define movement methods:
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    
    def move(self):
               
        # bounce off of top/bottom of screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.change_y *= -1
        elif self.rect.top < 0:
            self.change_y *= -1
            
        # reset when travels off screen on x axis
        # (update this when scoring & better reset are implemented)
        if self.rect.x <-600 or self.rect.x>(SCREEN_WIDTH+600):
            self.reset()
            
        # HIT DETECTION:
        self.rect.y += self.change_y # move up/down
        
        # check for collisions:
        puck_hit_player = pygame.sprite.spritecollide(self, player_list, False)
        if puck_hit_player:
            self.change_y *= -1
            self.rect.y += self.change_y
        
        self.rect.x += self.change_x # move left/right
        
        #check for collisions:
        puck_hit_player = pygame.sprite.spritecollide(self, player_list, False)
        if puck_hit_player:
            self.change_x *= -1
            self.rect.x += self.change_x
        for player in puck_hit_player:
            
            if player.change_y > 0: #if player was moving down:
               
                if self.change_y > 0: # if ball was moving down too
                    self.change_y *= 1.25
                    self.change_x*= .9
                else: 
                    self.change_y *= .9 # if the ball was going the other way, apply drag
                    self.change_x *= 1.25
                    
            elif player.change_y < 0:
                
                if self.change_y < 0:
                    self.change_y *= 1.25
                    self.change_x *= .9
                    
                else: 
                    self.change_y *= .9
                    self.change_x *= 1.25
                