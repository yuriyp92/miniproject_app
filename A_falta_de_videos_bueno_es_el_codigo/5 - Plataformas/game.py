import pygame
from settings import *
from map import Map
from player import Player

# IDEA: Usar la abeja como zombie en el juego top-down


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Plataformas & PEWPEWPEW")
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        # tiles
        self.wall_image = pygame.Surface((TILESIZE, TILESIZE))
        self.wall_image.fill(GREEN)
        self.spike_image = pygame.Surface((TILESIZE, TILESIZE))
        self.spike_image.fill(BROWN)
        self.save_point_image = pygame.Surface((TILESIZE, TILESIZE))
        self.save_point_image.fill(LIGHTGREY)
        self.trampoline_image = pygame.Surface((TILESIZE, TILESIZE))
        self.trampoline_image.fill(PINK)

        # player
        self.player_image = pygame.Surface((TILESIZE, TILESIZE))
        self.player_image.fill(ORANGE)

        # items
        self.coin_image = pygame.Surface((TILESIZE, TILESIZE))
        self.coin_image.fill(YELLOW)
        self.extralife_image = pygame.Surface((TILESIZE, TILESIZE))
        self.extralife_image.fill(RED)

        # mobs
        self.bee_image = pygame.Surface((TILESIZE, TILESIZE))
        self.bee_image.fill(PURPLE)

    def start(self):
        self.walls_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()
        self.mobs_group = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_map_from_file("sample.txt")
        self.current_map.create_sprites_from_data(self)

        x, y = self.current_map.entry_point
        self.player = Player(x, y,
                             (self.all_sprites), self.player_image,
                             self.on_player_dies)

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
        self.player.update(self.dt, self.walls_group)
        self.items_group.update(self.player)
        self.mobs_group.update(self.player)

    def draw(self):
        self.screen.fill(DARKBLUE)
        self.walls_group.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.items_group.draw(self.screen)
        self.mobs_group.draw(self.screen)
        pygame.display.flip()

    # game specifics - game engine

    def on_player_dies(self):
        self.player.teleport_to_save_point()


game = Game()
game.start()
