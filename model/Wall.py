import pygame
import enviroment


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.wall_layer
        self.groups = self.game.all_sprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(enviroment.blue)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
