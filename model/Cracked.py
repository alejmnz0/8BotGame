import pygame

from model import enviroment
from model.Item import Item


class Cracked(Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self._layer = enviroment.wall_layer
        self.groups = self.game.all_sprites, self.game.walls, self.game.breakable_objects
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.terrain_spritesheet.get_sprite(75, 0, self.width, self.height)
