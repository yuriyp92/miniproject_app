from tiles import Trampoline
from tiles import SavePoint
from settings import TILESIZE
from pygame import Vector2
from os import path
from settings import *
from tiles import *
from items import *



class Map():
    def __init__(self) -> None:
        self.map_data = []
        self.entry_point = Vector2(0,0)

    def load_map_from_file(self, filename):
        root_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(root_folder, 'assets', 'maps', filename), 'r') as file:
            for line in file:
                self.map_data.append(line)
    
    def create_sprites_from_data(self, game):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                position = Vector2(col,row) * TILESIZE
                if tile == '1':
                    Wall(col, row, game.walls_group, game.wall_image)
                if tile == 'P':
                    self.entry_point = position
                if tile == '*':
                    CoinItem(position.x, position.y, game.items_group, game.coin_image)
                if tile == 'v':
                    Spike(col, row, game.walls_group, game.spike_image)
                if tile == 's':
                    SavePoint(col, row, game.walls_group, game.save_point_image)
                if tile == 't':
                    Trampoline(col, row, game.walls_group, game.trampoline_image)