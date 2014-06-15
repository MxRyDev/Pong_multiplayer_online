import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Hello World')


# --- init Variables ---
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
