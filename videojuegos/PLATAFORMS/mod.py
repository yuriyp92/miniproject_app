import pygame
from pygame import Vector2

class Mob(pygame.sprite.Sprite):
    def __init__(self,x,y,groups,mob_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = mob_image