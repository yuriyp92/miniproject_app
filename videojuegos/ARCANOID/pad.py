from settings import PAD_WIDTH
from settings import PAD_ACCELERATION
from settings import DRAG
from settings import PAD_MAX_SPEED
from settings import BLUE
import pygame
from pygame import Vector2
from settings import *

class Pad(pygame.sprite.Sprite):
    def __init__(self,x,y,groups, pad_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = pad_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x,y)
        self.velocity = 0
    
    def update(self):
        self.keyboard_input()
        if self.rect.centerx < PAD_WIDTH//2:
            self.rect.centerx = PAD_WIDTH//2
            self.velocity *= 0.25
        if self.rect.centerx > WIDTH - PAD_WIDTH//2:
            self.rect.centerx = WIDTH - PAD_WIDTH//2
            self.velocity *= -0.25
        self.rect.centerx += self.velocity
    
    def keyboard_input(self):
        dx = 0  
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            dx = -1
        if keystate[pygame.K_RIGHT]:
            dx = 1
        
        self.velocity += dx * PAD_ACCELERATION
        self.velocity = max(-PAD_MAX_SPEED, min(PAD_MAX_SPEED,self.velocity))
        self.velocity -= self.velocity * DRAG
        if -1 < self.velocity < 1 and dx == 0:
            self.velocity = 0

    def hit(self, ball):
        offset = (self.rect.centerx - ball.rect.centerx)/(self.rect.width/2)
        ball.velocity.x = offset   
        ball.velocity.y *= -1 
        ball.rect.bottom = self.rect.top
        

        