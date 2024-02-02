import pygame.sprite
import enviroment
import math

import model.Diamond
import model.Bomb
import model.Water
import model.Heart


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.hp = 100
        self.inventory = []
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'
        self.animation_loop = 1
        self.width = enviroment.tilesize
        self.height = enviroment.tilesize
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.grab_item()
        self.take_damage()
        self.rect.x += self.x_change
        self.collide_block('x')
        self.rect.y += self.y_change
        self.collide_block('y')
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

    def collide_block(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                elif self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        elif direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                elif self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def grab_item(self):
        hits = pygame.sprite.spritecollide(self, self.game.items, True)
        if hits:
            match type(hits[0]):
                case model.Bomb.Bomb:
                    self.inventory.append('x')
                case model.Heart.Heart:
                    self.hp += enviroment.heart_healing

    def take_damage(self):
        hits = pygame.sprite.spritecollide(self, self.game.threats, False)
        if hits:
            match type(hits[0]):
                case model.Water.Water:
                    self.hp -= enviroment.water_damage
                    print(self.hp)
                    if self.hp <= 0:
                        self.game.running = False
                        self.game.playing = False


    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(25, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(50, 0, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(75, 0, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(100, 0, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(125, 0, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(225, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(250, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(275, 0, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(150, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(175, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(200, 0, self.width, self.height)]
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(75, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(225, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(150, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
