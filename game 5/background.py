import pygame
from game_parameters import *
import random


def draw_background(screen):
    #load our tiles from the assets folder
    water = pygame.image.load("../sprites/water.png").convert()
    sand = pygame.image.load("../sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../sprites/seagrass.png").convert()

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

    #draw the text
    text=custom_font.render("Chomp", True, (255,29,0))
    screen.blit(text, (screen_width/2-(text.get_width()/2),(text.get_height()-40)))