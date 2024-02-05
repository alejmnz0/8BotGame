import pygame.sprite
import enviroment
import math

import model.Diamond
import model.Bomb
import model.Water
import model.Heart
import model.Oxigen
from model.Cracked import Cracked
from model.Oxigen import Oxigen


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enviroment.player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * enviroment.tilesize
        self.y = y * enviroment.tilesize
        self.hp = enviroment.max_hp
        self.points = 0
        # self.inventory = []
        self.key_pressed = False
        self.dive_suit = False
        self.aquatic = False
        self.bombs = 0
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
        self.set_bomb()
        self.take_damage()
        self.change_suit()
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
                    self.bombs += 1
                case model.Heart.Heart:
                    if self.hp + enviroment.heart_healing > enviroment.max_hp:
                        self.hp = enviroment.max_hp
                    else:
                        self.hp += enviroment.heart_healing
                case model.Oxigen.Oxigen:
                    self.dive_suit = True
                case model.Diamond.Diamond:
                    self.points += 25
                    self.game.diamonds_remaining -= 1
                    if self.game.diamonds_remaining == 0:
                        self.game.show_win_screen()
                    sound = pygame.mixer.Sound(enviroment.coin_sound)
                    sound.play()

    def set_bomb(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and not enviroment.b_pressed and self.bombs > 0:
            sound = pygame.mixer.Sound(enviroment.bomb_sound)
            sound.play()
            enviroment.b_pressed = True
            self.bombs -= 1
            radius = enviroment.tilesize * 1.9

            for sprite in self.game.all_sprites:
                if isinstance(sprite, Cracked):
                    position_x, position_y = sprite.rect.x, sprite.rect.y
                    range_bomb = pygame.math.Vector2(position_x - self.rect.x, position_y - self.rect.y).length()

                    if range_bomb <= radius:
                        sprite.kill()
                if isinstance(sprite, Oxigen):
                    position_x, position_y = sprite.rect.x, sprite.rect.y
                    range_bomb = pygame.math.Vector2(position_x - self.rect.x, position_y - self.rect.y).length()

                    if range_bomb <= radius:
                        sprite.kill()


        elif not keys[pygame.K_b]:
            enviroment.b_pressed = False

    def change_suit(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and self.dive_suit and not enviroment.t_pressed:
            self.aquatic = not self.aquatic
            enviroment.t_pressed = True
        elif not keys[pygame.K_t]:
            enviroment.t_pressed = False

    def take_damage(self):
        hits = pygame.sprite.spritecollide(self, self.game.threats, False)
        if hits:
            match type(hits[0]):
                case model.Water.Water:
                    if not self.aquatic:
                        self.hp -= enviroment.water_damage
                        if self.hp <= 0:
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

        dive_down_animations = [self.game.dive_spritesheet.get_sprite(0, 0, self.width, self.height),
                                self.game.dive_spritesheet.get_sprite(25, 0, self.width, self.height),
                                self.game.dive_spritesheet.get_sprite(50, 0, self.width, self.height)]

        dive_up_animations = [self.game.dive_spritesheet.get_sprite(75, 0, self.width, self.height),
                              self.game.dive_spritesheet.get_sprite(100, 0, self.width, self.height),
                              self.game.dive_spritesheet.get_sprite(125, 0, self.width, self.height)]

        dive_left_animations = [self.game.dive_spritesheet.get_sprite(225, 0, self.width, self.height),
                                self.game.dive_spritesheet.get_sprite(250, 0, self.width, self.height),
                                self.game.dive_spritesheet.get_sprite(275, 0, self.width, self.height)]

        dive_right_animations = [self.game.dive_spritesheet.get_sprite(150, 0, self.width, self.height),
                                 self.game.dive_spritesheet.get_sprite(175, 0, self.width, self.height),
                                 self.game.dive_spritesheet.get_sprite(200, 0, self.width, self.height)]

        if self.facing == 'down':
            if self.y_change == 0:
                if not self.aquatic:
                    self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
                else:
                    self.image = self.game.dive_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                if not self.aquatic:
                    self.image = down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1
                else:
                    self.image = dive_down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                if not self.aquatic:
                    self.image = self.game.character_spritesheet.get_sprite(75, 0, self.width, self.height)
                else:
                    self.image = self.game.dive_spritesheet.get_sprite(75, 0, self.width, self.height)
            else:
                if not self.aquatic:
                    self.image = up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1
                else:
                    self.image = dive_up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                if not self.aquatic:
                    self.image = self.game.character_spritesheet.get_sprite(225, 0, self.width, self.height)
                else:
                    self.image = self.game.dive_spritesheet.get_sprite(225, 0, self.width, self.height)
            else:
                if not self.aquatic:
                    self.image = left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1
                else:
                    self.image = dive_left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                if not self.aquatic:
                    self.image = self.game.character_spritesheet.get_sprite(150, 0, self.width, self.height)
                else:
                    self.image = self.game.dive_spritesheet.get_sprite(150, 0, self.width, self.height)
            else:
                if not self.aquatic:
                    self.image = right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1
                else:
                    self.image = dive_right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1
