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
    def __init__(self):
        # init position variables
        self.impact = ''
        self.player_list = player_list
        self.choices = [PUCK_SPEED, -1*PUCK_SPEED]
        self.change_x = choice(self.choices)
        self.change_y = randint(-1*PUCK_SPEED, PUCK_SPEED)
        self.passed_player = False
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
        
    # Define movement methods:
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
        
        # check if puck has passed a player 'x' face
        if self.change_x > 0: # moving right
            if self.rect.right >= SCREEN_WIDTH - (50+PLAYER_WIDTH):
                self.passed = True
                print('passed')
        elif self.chage_x < 0: # moving left
            if self.rect.left >= 50 + PLAYER_WIDTH:
                self.passed = True
                print('passed')
        else: self.passed = False
        
    def reverse_x(self):
        self.change_x *= -1
        
    def reverse_y(self):
        self.change_y *= -1
        
    
    def move(self, plist):
        
        # check to see if puck has passed a player.
        p1 = plist[0]
        p2 = plist[1]
        # check right player:
        if self.rect.right >= p1.rect.left:
            #passed on top:
            if self.rect.bottom < p1.rect.top:
                self.passed_player = True
                self.impact = 'top'
            #passed on bottom
            elif self.rect.top > p1.rect.bottom:
                self.passed_player = True
                self.impact = 'bottom'
        # check left player:
        elif self.rect.left <= p2.rect.right:
            #passed on top:
            if self.rect.bottom < p2.rect.top:
                self.passed_player= True
                self.impact = 'top'
            #passed on bottom:
            elif self.rect.top > p2.rect.bottom:
                self.passed_player = True
                self.impact = 'bottom'
            
        
        
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
            
            
        # collision test:
        
        #puck hits side of player
        puck_hit_player = pygame.sprite.spritecollide(self, p_list, False)
        for player in puck_hit_player:
            
            # figure out buffer:
            if player.rect.x > SCREEN_WIDTH/2: # if its the right player:
                buffx = -(self.rect.right - player.rect.left)
            else:
                buffx = (self.rect.right - player.rect.left)
            
            if self.impact == 'top':
                buffy = (self.rect.bottom - player.rect.top)
            elif self.impact == 'bottom':
                buffy = (self.rect.top - player.rect.bottom)
            
            if self.passed_player:
                self.reverse_y()
                self.rect.y += buffy
            else:
                self.reverse_x()
                self.rect.x += buffx
            self.passed_player = False