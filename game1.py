import pygame
import sys
import random
#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#creat the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("using blit to draw tile")

def draw_background(screen):
    #load our tiles from the assets folder
    water = pygame.image.load("sprites/water.png").convert()
    sand = pygame.image.load("sprites/sand_top.png").convert()
    seagrass = pygame.image.load("sprites/seagrass.png").convert()
    #make pngs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen with water
    for x in range(0,screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))
    #fill in sand
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x,screen_height-tile_size))

    #fill in seagrass
    for _ in range (8):
        x=random.randint(0, screen_width)
        screen.blit(seagrass, (x,screen_height-(tile_size+20)))
# Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the background
    screen.blit(background, (0,0))

    pygame.display.flip()

pygame.QUIT