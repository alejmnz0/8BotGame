import pygame.sprite
import enviroment


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.ground_layer
        self.groups = self.game.all_sprites, self.game.threats
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize
        self.image = self.game.terrain_spritesheet.get_sprite(25, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
