from settings import TILESIZE
import pygame
from settings import *
from pygame import Vector2

class Wall(pygame.sprite.Sprite):
    def __init__(self, tile_x,tile_y, groups, wall_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = wall_image
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(tile_x, tile_y) * TILESIZE