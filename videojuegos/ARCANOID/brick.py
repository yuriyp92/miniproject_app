from settings import BLUE, BROWN, YELLOW
import pygame
import random
from settings import *
from pygame import Vector2

class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y, groups, brick_images, break_fx):
        pygame.sprite.Sprite.__init__(self,groups)
        self.image = (random.choice(brick_images))
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(x,y)
        self.break_fx = break_fx
    def breakit(self):
        self.break_fx.play()
        self.kill()