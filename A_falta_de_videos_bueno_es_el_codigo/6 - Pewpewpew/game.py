import pygame
from settings import *
from map import Map
from player import Player


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Plataformas & PEWPEWPEW")
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        self.wall_image = pygame.Surface((TILESIZE, TILESIZE))
        self.wall_image.fill(GREEN)
        self.player_image = pygame.Surface((TILESIZE, TILESIZE))
        self.player_image.fill(ORANGE)

    def start(self):
        self.walls_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_map_from_file("sample.txt")
        self.current_map.create_sprites_from_data(self)

        x, y = self.current_map.entry_point
        self.player = Player(x, y,
                             (self.all_sprites), self.player_image)

        self.run()

    def run(self):
        self.isPlaying = True
        while (self.isPlaying):
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.player.update(self.walls_group)

    def draw(self):
        self.screen.fill(DARKBLUE)
        self.walls_group.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


game = Game()
game.start()
