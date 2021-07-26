import pygame
from settings import *
from pygame import Vector2
import math

from snake import Snake
from fruit import Fruit

# - Juego en una rejilla de celdas 16x16
# - Clon del Snake clásico del Nokia
# - Controlamos la CABEZA de una serpiente que CRECE al comer FRUTA
# - Un pieza de FRUTA aparece aletoriamente un punto de la regilla
# - Al comernosla, la serpiente CRECE y la fruta reaparece en otro sitio
# - Por cada pieza de fruta ganamos 1 PUNTO, que se acumulan
# - Por cada pieza de fruta que comamos aumente LA DIFICULTAD
# - La partida termina si chocamos con nuestro propio cuerpo, mostrando
#   al jugador la PUNTUACIÓN obtenida

# MEJORA: añadir un mapa contra el que podemos chocar


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont('arial', 32)

    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.snake = Snake(10, 10, self.all_sprites)
        self.fruit = Fruit((self.all_sprites, self.fruits))
        self.score = 0
        self.run()

    def run(self):
        self.playing = True
        while (self.playing):
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.game_over_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.snake, self.fruits, False)
        for hit in hits:
            self.snake.grow(3)
            hit.teleport()
            self.score += 1
        self.playing = self.snake.is_alive

    def draw(self):
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y))
        self.snake.draw_tail(self.screen)
        self.all_sprites.draw(self.screen)

        score_text = self.small_font.render(
            f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (5, 5))
        pygame.display.flip()

    #
    #  MAIN MENU & GAME OVER SCREENS
    #

    def main_menu(self):
        title_text = self.large_font.render("SNAKE", True, WHITE)
        instructions_text = self.small_font.render(
            "Press any key to begin", True, LIGHGREY)

        self.screen.fill(BLACK)
        self.screen.blit(
            title_text, (WIDTH//2 - title_text.get_rect().width//2, 25))
        self.screen.blit(
            instructions_text, (
                WIDTH//2 - instructions_text.get_rect().width//2, HEIGHT-50)
        )

        pygame.display.flip()

        in_main_menu = True
        while (in_main_menu):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
        self.start()

    def game_over_menu(self):
        title_text = self.large_font.render("GAME OVER", True, RED)
        instructions_text = self.small_font.render(
            "Press any key to restart", True, LIGHGREY)

        self.screen.fill(BLACK)
        self.screen.blit(
            title_text, (WIDTH//2 - title_text.get_rect().width//2, 25))

        score_text = self.small_font.render(
            f"Score: {self.score}", True, WHITE)
        self.screen.blit(
            score_text, (WIDTH//2 - score_text.get_rect().width//2, HEIGHT//2))

        self.screen.blit(
            instructions_text, (
                WIDTH//2 - instructions_text.get_rect().width//2, HEIGHT-50)
        )

        pygame.display.flip()

        in_game_over_menu = True
        while (in_game_over_menu):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_game_over_menu = False
        self.main_menu()


game = Game()
game.main_menu()
