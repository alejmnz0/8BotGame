import pygame

import enviroment


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):

        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(enviroment.blue)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
