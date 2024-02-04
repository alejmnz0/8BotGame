import pygame

from model.Item import Item


class Heart(Item):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.objects_spritesheet.get_sprite(75, 0, self.width, self.height)
