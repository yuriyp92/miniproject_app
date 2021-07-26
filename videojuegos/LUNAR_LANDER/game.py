from settings import HEIGHT
from settings import DARKGREY
from settings import BLACK
import pygame
from settings import *
from pygame import Vector2
from rocket import Rocket
from moon import Moon

#REGLAS
# Juego arcade
# El jugador controla un cohete que debe aterrizar SUAVEMENTE
# Controla el cohete con los cursores
# Al cohete tiene mucha inercia
# El cohete tiene COMBUSTIBLE que se gasta al impulsar el cohete
# Si el combustible se agota, el cohete deja de poder ser controlado
# El juego acaba MAL si chocamos
# El juego acaba BIEN si aterrizamos en la ZONA DE ATERRIZAJE


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Lunar Lander")
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):
        self.rocket = Rocket(WIDTH/2, 0)
        self.moon = Moon(HEIGHT/3, 10)
        self.moon.generate_terrain()
    
    def run(self):
        self.playing = True
        while (self.playing):
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.playing = False
       

    def update(self):
        self.rocket.update(self.moon)
        if not self.rocket.alive:
            self.playing = False
            pass # game over
        if self.rocket.landed:
            self.start()

    def draw(self):
        self.screen.fill(BLACK)
        self.rocket.draw(self.screen)
        self.moon.draw(self.screen)
        self.draw_UI()
        pygame.display.flip()
    
    def draw_UI(self):
        pygame.draw.rect(self.screen, DARKGREY, pygame.Rect(5,5,200,25))
        pygame.draw.rect(self.screen, LIGHTGREY, pygame.Rect(7,7,196*self.rocket.fuel,21))

game = Game()
game.run()