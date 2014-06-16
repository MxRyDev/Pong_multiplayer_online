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
from player_class import *


    
# PUCK CLASS
class Puck(pygame.sprite.Sprite):
    def __init__(self):
        # init position variables
        self.choices = [PUCK_SPEED, -1*PUCK_SPEED]
        self.change_x = choice(self.choices)
        self.change_y = randint(-1*PUCK_SPEED, PUCK_SPEED)
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
            
        puck_hit_player = pygame.sprite.spritecollide(self, player_list, False)
        for puck in puck_hit_player:
            if self.change_x < 0:
                self.change_x *= -1
        
           