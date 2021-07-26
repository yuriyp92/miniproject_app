import pygame
from pygame import Vector2


class Item (pygame.sprite.Sprite):
    def __init__(self, x, y, groups, item_name, item_image):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = item_image
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(x, y)
        self.name = item_name
        self.groups = groups

    def update(self, player):
        self.check_hits(player)

    def check_hits(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.picked_by(player)
            self.kill()

    def picked_by(self,  player):
        print(f"item picked up!")


class CoinItem(Item):
    def __init__(self, x, y, groups, item_image):
        super().__init__(x, y, groups, "Coin", item_image)

    def picked_by(self, player):
        print(f"coin picked up!")


class ExtraLifeItem(Item):
    def __init__(self, x, y, groups, item_image):
        super().__init__(x, y, groups, "Extra life", item_image)

    def picked_by(self, player):
        print(f"extra life picked up!")
