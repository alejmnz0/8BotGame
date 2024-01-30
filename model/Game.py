import pygame
import enviroment
from model.Player import Player
from model.Spritesheet import Spritesheet
from model.Wall import Wall


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([enviroment.width, enviroment.height])
        self.clock = pygame.time.Clock()
        self.running = True
        self.character_spritesheet = Spritesheet(enviroment.character_sprites)
        self.terrain_spritesheet = Spritesheet(enviroment.terrain_sprites)

    def new_game(self, tilemap):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 1, 2)
        self.create_map(tilemap)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(enviroment.black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(enviroment.fps)
        pygame.display.update()

    def create_map(self, tilemap):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == 'b':
                    Wall(self, j, i)
