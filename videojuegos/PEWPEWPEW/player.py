import pygame
from settings import *
from pygame import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, player_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(x,y)

        self.velocity = Vector2(0,0)
        self.desired_velocity = Vector2(0,0)

    def update(self, walls_group):
        self.handle_input()
        self.velocity -= self.velocity * WORLD['DRAG']
        self.velocity += self.desired_velocity
        if self.velocity.magnitude() < 1:
            self.velocity = Vector2(0,0)
        position = self.rect.center + self.velocity * PLAYER['MAX_SPEED']

        self.rect.centerx = position.x
        self.collition_with_walls('x', walls_group)
        self.rect.centery = position.y
        self.collition_with_walls('y', walls_group)


    def handle_input(self):
        delta = Vector2(0,0)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            delta.x = -1
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            delta.x = 1
        if key[pygame.K_UP] or key[pygame.K_w]:
            delta.y = -1
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            delta.y = 1

        self.desired_velocity = delta

    def collition_with_walls(self, dir, walls_group):
        hits = pygame.sprite.spritecollide(self, walls_group, False)
        if len(hits) == 0:
            return
        hit_rect = hits[0].rect
        
        if dir == 'x':
            if self.velocity.x > 0:
                self.rect.right = hit_rect.left
            if self.velocity.x < 0:
                self.rect.left = hit_rect.right
        self.velocity.x = 0
        
        if dir == 'y':
            if self.velocity.y > 0:
                self.rect.bottom = hit_rect.top
            if self.velocity.y < 0:
                self.rect.top = hit_rect.bottom
        self.velocity.y = 0
        