import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
running = True
# App Name
pygame.display.set_caption('CakeMaker')

clock = pygame.time.Clock()

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()