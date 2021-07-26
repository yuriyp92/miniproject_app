import pygame
from settings import *
from pygame import Vector2


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_x, tile_y, groups, tile_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = tile_image
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(tile_x, tile_y) * TILESIZE

    def stepped_on(self, mob):
        pass


class Wall(Tile):
    def __init__(self, tile_x, tile_y, groups, wall_image):
        super().__init__(tile_x, tile_y, groups, wall_image)


class Spike(Tile):
    def __init__(self, tile_x, tile_y, groups, spike_image):
        super().__init__(tile_x, tile_y, groups, spike_image)

    def stepped_on(self, mob):
        mob.die()


class SavePoint(Tile):
    def __init__(self, tile_x, tile_y, groups, save_point_image):
        super().__init__(tile_x, tile_y, groups, save_point_image)

    def stepped_on(self, mob):
        mob.update_save_point(self.rect.left, self.rect.top - TILESIZE)


class Trampoline(Tile):
    def __init__(self, tile_x, tile_y, groups, trampoline_image):
        super().__init__(tile_x, tile_y, groups, trampoline_image)

    def stepped_on(self, mob):
        mob.push(Vector2(5, -15))
