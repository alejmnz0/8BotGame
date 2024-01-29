import pygame
import enviroment
from model.Player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([enviroment.width, enviroment.height])
        self.clock = pygame.time.Clock()
        self.running = True

    def new_game(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 1, 2)

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