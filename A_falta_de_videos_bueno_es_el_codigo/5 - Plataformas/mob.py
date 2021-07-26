import pygame
from pygame import Vector2
from settings import *
import math
import random


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, mob_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = mob_image
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(x, y)

        self.desired_velocity = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.speed = 0
        self.position = Vector2(x, y)

    def update(self, player):
        pass

    def move(self):
        self.velocity += self.desired_velocity
        self.velocity -= self.velocity * WORLD['DRAG']
        self.position = self.position + self.velocity * self.speed
        self.rect.center = self.position


class Bee(Mob):
    def __init__(self, x, y, groups, bee_image):
        super().__init__(x, y, groups, bee_image)
        self.speed = MOBS['BEE']['SPEED']

    def update(self, player):
        towards_player = Vector2(player.rect.centerx - self.rect.centerx,
                                 player.rect.centery - self.rect.centery)
        if towards_player.magnitude() < MOBS['BEE']['SIGHT_RANGE']:
            self.desired_velocity = towards_player.normalize()
        else:
            self.desired_velocity = Vector2(
                random.uniform(-1, 2), random.uniform(-1, 2)).normalize()

        self.move()

        if pygame.sprite.collide_rect(self, player):
            player.die()
