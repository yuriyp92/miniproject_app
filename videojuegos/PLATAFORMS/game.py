from settings import BLUE
from settings import BROWN
from settings import YELLOW
from settings import BLUISHGREY
from settings import BLACK, TILESIZE
from map import Map
from settings import *
import pygame
from player import Player


class Game():
    def __init__(self) -> None: 
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Plataformas & PEWPEWPEW')
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        self.wall_image = pygame.Surface((TILESIZE,TILESIZE))
        self.wall_image.fill(GREEN)

        self.player_image = pygame.Surface((TILESIZE,TILESIZE))
        self.player_image.fill(ORANGE)

        self.coin_image = pygame.Surface((TILESIZE,TILESIZE))
        self.coin_image.fill(YELLOW)

        self.spike_image = pygame.Surface((TILESIZE,TILESIZE))
        self.spike_image.fill(BROWN)

        self.save_point_image = pygame.Surface((TILESIZE,TILESIZE))
        self.save_point_image.fill(BLUE)

        self.trampoline_image = pygame.Surface((TILESIZE,TILESIZE))
        self.trampoline_image.fill(BLUISHGREY)

    def start(self):
        self.walls_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_map_from_file('sample.txt')
        self.current_map.create_sprites_from_data(self)

        x,y = self.current_map.entry_point
        self.player = Player(x,y,self.all_sprites,self.player_image,self.on_player_dies)

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
    
    def draw(self):
        self.screen.fill(BLACK)
        self.walls_group.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.items_group.draw(self.screen)
        pygame.display.flip()

    def on_player_dies(self):
        self.player.teleport_to_save_point()

    

game = Game()
game.start()