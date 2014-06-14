import pygame
import random
import sys
from pygame.locals import *
pygame.init()

# --- Constants ---
# color:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# screen:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
SCREEN_SIZE = ([SCREEN_WIDTH, SCREEN_HEIGHT])
screen = pygame.display.set_mode(SCREEN_SIZE)

# pos/speed/quantity:
PADDLE_SPEED = 5
BALL_SPEED = 15

# --- init Variables ---
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# p1:
p1_speedy = 0
p1_keyspressed = 0
p1_direct = 'left'

# p2:
p2_speedy = 0
p2_keyspressed = 0
p2_direct = 'right'

# both:
change_y = 0
is_dead = False

# ---  Create Lists  ---
# (for collision detection)
p1_list = pygame.sprite.Group()
p2_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_bullets_list = pygame.sprite.Group()
ball_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# _____________________________________________________________________________
# --------------------------- CLASSES FOR GAME OBJECTS ------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Player class
class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, player_list):
        self.player_list = player_list
        self.change_y = 0

        pygame.sprite.Sprite.__init__(self)
        
        # Create image
        self.image = pygame.Surface([10, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # add to list
        all_sprites_list.add(self)
        self.player_list.add(self)
    
    def changespeed(self, y):
        self.change_y += y
            
    
    def move(self, wall_list = wall_list):

        # move up/down
        self.rect.y += self.change_y

        # keep player on the screen
        if self.rect.x >= SCREEN_WIDTH - 15:
            self.rect.x = SCREEN_WIDTH - 15
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= SCREEN_HEIGHT - 15:
            self.rect.y = SCREEN_HEIGHT - 15
        if self.rect.y <= 0:
            self.rect.y = 0
            
    def remove(self):
        all_sprites_list.remove(self)
        all_bullets_list.remove(self)
        self.firing_players_list.remove(self)
        print('bullet removed')


# _____________________________________________________________________________
# ---------------------------- CREATE GAME OBJECTS ----------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create players
paddle_1 = Paddle(RED, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200, p1_list)
paddle_2 = Paddle(GREEN, 50, 200, p2_list)



done = False

while not done:
    for event in pygame.event.get():
        # Handle closing the window    
        if event.type == pygame.QUIT:
            done = True
        # Process 'player pushing key':
        elif event.type == pygame.KEYDOWN:
            # paddle 1 (moving):
            if event.key == pygame.K_UP:
                paddle_1.changespeed((-1*PADDLE_SPEED))
                p1_direct = 'up'
                p1_keyspressed += 1
            elif event.key == pygame.K_DOWN:
                paddle_1.changespeed(PADDLE_SPEED)
                p1_direct = 'down'
                p1_keyspressed += 1
        # Procces 'player lifting key':
        # paddle 1:
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle_1.changespeed(PADDLE_SPEED)
                p1_keyspressed -= 1
            elif event.key == pygame.K_DOWN:
                paddle_1.changespeed((-1*PADDLE_SPEED))
                p1_keyspressed -= 1

    # --- MOVE OBJECTS ---
    # ______________________
    # move players and their bullets
    paddle_1.move()
    paddle_2.move()
    
    # --- DRAW SCREEN ---
    # ___________________
    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
