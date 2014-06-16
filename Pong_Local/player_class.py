# Defines the player class to be imported into pong/MAIN

if __name__ == '__main__':
    print('''
    This file is used to define the PLAYER class for Local Pong.
    it is to be used within "localpong_main.py".
    on its own, it provides no functionality.
    
    HAFF A GUD DAY
    ''')
    
import pygame.sprite
from constants import *



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