import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player
# Initialize pygame
pygame.init()
green_fish="../sprites/green_fish.png"
#Create the Screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Adding a player fish")

#add pygame clock
clock = pygame.time.Clock()

#score
score_font=pygame.font.Font('../fonts/Black_Crayon.ttf', 25)
score=0

#sounds
oof=pygame.mixer.Sound('../fonts/hurt.wav')

#Draw player class
player = Player(screen_width/2,screen_height/2)

#Main Loop
running=True
background =screen.copy()
draw_background(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_height, screen_width*2), random.randint(80, screen_height - (2*tile_size))))



#placeholder

while running:
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            running = False
        player.stop()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                player.move_up()
            if event.key==pygame.K_DOWN:
                player.move_down()
            if event.key==pygame.K_LEFT:
                player.move_left()
            if event.key==pygame.K_RIGHT:
                player.move_right()
    # draw the background
    screen.blit(background, (0, 0))

    # update fish position
    fishes.update()

    #update player fish
    player.update()
    result=pygame.sprite.spritecollide(player, fishes, True)
    if result:
        pygame.mixer.Sound.play(oof)
        for x in result:
            score=score+1
        for _ in range(len(result)):
            fishes.add(Fish(random.randint(screen_width, screen_width + tile_size), random.randint(tile_size, 400)))
    # check if fish have left the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),random.randint(80, screen_height - (2 * tile_size))))
    fishes.draw(screen)


    score_text=score_font.render(f"Score: {score}", True, (255,0,0))
    screen.blit(score_text, (screen_width - score_text.get_width()-5, 10))


    #draw player fish
    player.draw(screen)
    pygame.display.flip()
    #set frame rate
    clock.tick(60)
pygame.quit()
sys.exit()