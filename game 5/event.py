import pygame
import sys

from game_parameters import *
from background import draw_background

#initialize pygame
pygame.init()

#create screen
#create the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("using blit to draw tile")


#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print ('k up')
            if event.key==pygame.K_DOWN:
                print ('k down')
            if event.key==pygame.K_LEFT:
                print ('k left')
            if event.key==pygame.K_RIGHT:
                print ('k right')



    #draw background
    screen.blit(background,(0,0))
    #update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
