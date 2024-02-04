import pygame

from model.Item import Item


class Bomb(Item):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.objects_spritesheet.get_sprite(50, 0, self.width, self.height)
        self.radius_explotion = (self)

    def collide_blocks(self):
        self.x += 10
        self.y += 10
        hits = pygame.sprite.spritecollide(self, self.game.breakable_objects, True)
