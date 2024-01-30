import pygame.sprite
import enviroment


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x_change += enviroment.player_speed
            self.facing = 'right'
        if keys[pygame.K_a]:
            self.x_change -= enviroment.player_speed
            self.facing = 'left'
        if keys[pygame.K_w]:
            self.y_change -= enviroment.player_speed
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += enviroment.player_speed
            self.facing = 'down'
