import pygame

from model import enviroment


class Cracked(pygame.sprite.Sprite):

    # def __init__(self, game, x, y):
    #     super().__init__(game, x, y)
    #     self._layer = enviroment.wall_layer
    #     self.groups = self.game.all_sprites, self.game.walls, self.game.breakable_objects
    #     pygame.sprite.Sprite.__init__(self, self.groups)
    #     self.image = self.game.terrain_spritesheet.get_sprite(75, 0, self.width, self.height)

    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.wall_layer
        self.groups = self.game.all_sprites, self.game.walls, self.game.breakable_objects
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize
        self.image = self.game.terrain_spritesheet.get_sprite(75, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
