#pyagme sprite class for a player fish

import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../sprites/wooden.png").convert()
        self.forward_image.set_colorkey((0, 0, 0))
        self.back_image = pygame.transform.flip(self.forward_image, True, False)
        self.back_image.set_colorkey((0, 0, 0))
        self.image=self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed=0
        self.y_speed=0

    def move_up(self):
        self.y_speed = -PLAYER_SPEED
    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed= -PLAYER_SPEED
        self.image=self.back_image
    def move_right(self):
        self.x_speed=PLAYER_SPEED
        self.image=self.forward_image

    def stop(self):
        self.x_speed=0
        self.y_speed=0

    def update(self):
        #TODO need to check if player fish went off the screen
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x=self.x
        self.rect.y=self.y
        if self.rect.x < 0:
            self.x_speed = PLAYER_SPEED
            self.image = self.forward_image
        if self.rect.x>screen_width-tile_size:
            self.x_speed = -PLAYER_SPEED
            self.image = self.back_image
        if self.rect.y < 0:
            self.y_speed = PLAYER_SPEED
        if self.rect.y> screen_height-tile_size:
            self.y_speed = -PLAYER_SPEED


    def draw(self, screen):
        screen.blit(self.image, self.rect)