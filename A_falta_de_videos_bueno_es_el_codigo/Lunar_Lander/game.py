import pygame
from settings import *
from pygame import Vector2
import math

from rocket import Rocket
from moon import Moon

# REGLAS:
# - Juego arcade
# - El jugador controla un cohete que debe hacer aterrizar SUAVEMENTE
# - Controla el COHETE con los CURSORES
# - Al cohete le afecta la fuerza de GRAVEDAD
# - EL cohete tiene mucha INERCIA
# - El cohete tiene COMBUSTIBLE, que se gasta al impulsar el cohete
# - Si el combustible se agota, el cohete deja de poder ser controlado
# - El juego acaba MAL si chocamos contra el SUELO
# - El juego acaba BIEN si aterrizamos en la ZONA DE ATERRIZAJE

# - Podría haber distinta gravedad o ser aleatoria al llegar a un nuevo planeta
# - Podría haber corrientes de aire de distinta intensidad
# - Podríamos medir cómo de bien se ha hecho en base al tiempo y el combustible restante
# - Podríamos recoger gas en el descenso para aumentar la puntuación o para recuperar combustible
# - Podría haber obstáculos en el aire que tenemos que evitar


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):
        self.rocket = Rocket(WIDTH/2, 0)
        self.moon = Moon(HEIGHT//2, 10)
        self.moon.generate_terrain()

    def run(self):
        self.playing = True
        while (self.playing):
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.rocket.update(self.moon)
        
        if not self.rocket.alive:
            self.playing = False

        if self.rocket.landed:
            self.start()

    def draw(self):
        self.screen.fill(BLACK)
        self.rocket.draw(self.screen)
        self.moon.draw(self.screen)
        self.draw_UI()
        pygame.display.flip()

    def draw_UI(self):
        pygame.draw.rect(self.screen, MIDGREY, pygame.Rect(5, 5, 200, 25))
        pygame.draw.rect(self.screen, LIGHTGREY, pygame.Rect(
            7, 7, 196 * self.rocket.fuel, 21))


game = Game()
game.run()
