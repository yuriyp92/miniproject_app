from settings import LIGHTGREY
from fruit import Fruit
from settings import GRID_HEIGHT
from settings import WIDTH
from settings import GRID_WIDTH, HEIGHT, MIDGREY, TILESIZE
from settings import BLACK
from settings import WHITE
from settings import *
import pygame
from pygame import Vector2
import time
from snake import Snake
# Juego en una rejilla de 16 x 16:
# Clon del clásico del Nokia

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.large_font = pygame.font.SysFont("arial",100)
        self.small_font = pygame.font.SysFont("arial",32)
    
    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.snake = Snake(10,10, self.all_sprites)
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
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.snake,self.fruits,False)
        for hit in hits:
            self.snake.grow(1)
            hit.teleport()
            self.score += 1
        self.playing = self.snake.is_alive
        

    def draw(self):
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, MIDGREY, (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, MIDGREY, (0,y), (WIDTH,y))
        self.all_sprites.draw(self.screen)
        self.snake.draw_tail(self.screen)
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, ((WIDTH//2 - score_text.get_rect().width//2),25))
        pygame.display.flip()

    #
    # MAIN MENU & GAME OVER SCREENS
    #
    def main_menu(self):
        title_text = self.large_font.render("SNAKE", True, WHITE)
        instructions_text = self.small_font.render("Press any key to begin", True, LIGHTGREY)
        self.screen.fill(BLACK)
        self.screen.blit(title_text, ((WIDTH//2 - title_text.get_rect().width//2),25))
        self.screen.blit(instructions_text, ((WIDTH//2 - title_text.get_rect().width//2),HEIGHT -50))
        in_main_menu = True
        pygame.display.flip()
        while (in_main_menu):
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type == pygame.KEYDOWN:
                    in_main_menu = False
        self.start()
    
    def game_over_menu(self):
        title_text = self.large_font.render("GAME OVER", True, RED)
        instructions_text = self.small_font.render("Press any key to restart", True, LIGHTGREY)
        self.screen.fill(BLACK)
        self.screen.blit(title_text, ((WIDTH//2 - title_text.get_rect().width//2),25))
        self.screen.blit(instructions_text, ((WIDTH//2 - title_text.get_rect().width//2),HEIGHT-50))
        in_game_over_menu = True
        pygame.display.flip()
        while (in_game_over_menu):
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type == pygame.KEYDOWN:
                    in_game_over_menu= False
        self.main_menu()
   
game = Game()
game.main_menu()