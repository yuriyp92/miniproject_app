from settings import BLACK
from settings import WHITE
from settings import *
import pygame
from pygame import Vector2

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([640, 480])
        pygame.display.set_caption("una cara")
        
    
    def run(self):
        self.playing = True
        while (self.playing):
            self.events()
            self.update()
            self.draw()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.playing = False
        pass

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, RED, Vector2(320, 260),150)
        pygame.draw.circle(self.screen, WHITE, Vector2(280, 2   20),30)
        pygame.draw.circle(self.screen, WHITE, Vector2(360, 220),30)
        pygame.draw.circle(self.screen, BLACK, Vector2(280, 220),10)
        pygame.draw.circle(self.screen, BLACK, Vector2(360, 220),10)
        pygame.draw.line(self.screen,
            WHITE,
            Vector2(120,150),
            Vector2(520,150),
            3)
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(220, 50, 200, 100))
        pygame.display.flip()
        pygame.draw.line(self.screen,
            WHITE,
            Vector2(320,350),
            Vector2(420,350),
            20)

game = Game()
game.run()