import pygame
from settings import *
from pygame import Vector2
import math


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)

    def run(self):
        self.playing = True
        while (self.playing):
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        # ears
        pygame.draw.circle(self.screen, BROWN, Vector2(240, 160), 75)
        pygame.draw.circle(self.screen, BROWN, Vector2(400, 160), 75)
        pygame.draw.circle(self.screen, DARKBROWN, Vector2(240, 160), 50)
        pygame.draw.circle(self.screen, DARKBROWN, Vector2(400, 160), 50)

        # head
        pygame.draw.circle(self.screen, BROWN, Vector2(320, 240), 125)
        pygame.draw.ellipse(self.screen, BROWN,
                            pygame.Rect(180, 200, 280, 170), 0)

        # eyes
        pygame.draw.circle(self.screen, DARKGREY, Vector2(250, 240), 25)
        pygame.draw.circle(self.screen, DARKGREY, Vector2(390, 240), 25)
        pygame.draw.circle(self.screen, WHITE, Vector2(240, 230), 5)
        pygame.draw.circle(self.screen, WHITE, Vector2(380, 230), 5)

        # nose
        pygame.draw.circle(self.screen, DARKGREY, Vector2(320, 260), 15)

        # mouth
        pygame.draw.arc(self.screen, DARKGREY, pygame.Rect(
            295, 270, 50, 35), math.radians(180), 0, 3)

        pygame.display.flip()


game = Game()
game.run()
