import pygame

from model import enviroment


class Oxigen(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize
        self.image = self.game.objects_spritesheet.get_sprite(25, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
