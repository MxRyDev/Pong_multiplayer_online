import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Hello World')

# Colors
RED = (255, 0, 0)

# --- init Variables ---
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
wall_1 = pygame.Rect(10, 20, 200, 500)
pygame.draw.rect(screen, RED, (200, 150, 100, 50))

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
