import pygame
import sys
import random
from fish import Fish, fishes
#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#add pygame clock
clock = pygame.time.Clock()

#create the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("using blit to draw tile")
#load game font
custom_font=pygame.font.Font("fonts/4MyLover.ttf", 60)

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

    #draw the text
    text=custom_font.render("Chomp", True, (255,29,0))
    screen.blit(text, (screen_width/2-(text.get_width()/2),(text.get_height()-40)))





# Main loop
running = True
background = screen.copy()
draw_background(background)
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(80, screen_height - (2*tile_size))))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the background
    screen.blit(background, (0,0))

    #update fish positionm
    fishes.update()

    #check if fish have left the screen
    for fish in fishes:
        if fish.rect.x<-fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width+50),random.randint(80, screen_height - (2 * tile_size))))
    fishes.draw(screen)
    pygame.display.flip()
    #set frame rate
    clock.tick(60)
pygame.QUIT