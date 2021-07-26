from os import path
from settings import *
from pygame import Vector2
from tiles import *


class Map:
    def __init__(self):
        self.map_data = []
        self.entry_point = Vector2(0, 0)

    def load_map_from_file(self, filename):
        root_folder = path.dirname(__file__)
        self.map_data = []

        with open(path.join(root_folder, "assets", "maps", filename), 'r') as file:
            for line in file:
                self.map_data.append(line)

    def create_sprites_from_data(self, game):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                position = Vector2(col, row) * TILESIZE
                if tile == '1':
                    Wall(col, row, game.walls_group, game.wall_image)
                if tile == 'P':
                    self.entry_point = position
