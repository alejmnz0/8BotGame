import random

import pygame
import enviroment
from model.Diamond import Diamond
from model.Heart import Heart
from model.Oxigen import Oxigen
from model.Player import Player
from model.Spritesheet import Spritesheet
from model.Wall import Wall
from model.Ground import Ground
from model.Water import Water
from model.Bomb import Bomb


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([enviroment.width, enviroment.height])
        self.clock = pygame.time.Clock()
        self.running = True
        self.character_spritesheet = Spritesheet(enviroment.character_sprites)
        self.terrain_spritesheet = Spritesheet(enviroment.terrain_sprites)
        self.objects_spritesheet = Spritesheet(enviroment.objects_sprites)

    def new_game(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.threats = pygame.sprite.LayeredUpdates()
        self.create_map()
        self.play_music()

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

    def create_map(self):
        tilemap1 = open(enviroment.file).read().split("\n")
        tilemap2 = []
        for x in tilemap1:
            tilemap2.append(x.split(','))

        print(tilemap2)
        random_objects = []
        for x in tilemap2[-1]:
            random_objects.append(x.split(':'))
        bombs = int(random_objects[0][1])
        hearts = int(random_objects[1][1])
        diamonds = int(random_objects[2][1])

        tilemap2 = self.randomize_objects(tilemap2, bombs, 'x')
        tilemap2 = self.randomize_objects(tilemap2, hearts, 'h')
        tilemap2 = self.randomize_objects(tilemap2, diamonds, 'd')

        for i, row in enumerate(tilemap2):
            for j, column in enumerate(row):
                if column == 'b':
                    Wall(self, j, i)
                elif column == '-':
                    Ground(self, j, i)
                elif column == 'w':
                    Water(self, j, i)
                elif column == 'x':
                    Ground(self, j, i)
                    Bomb(self, j, i)
                elif column == 'h':
                    Ground(self, j, i)
                    Heart(self, j, i)
                elif column == 'o':
                    Ground(self, j, i)
                    Oxigen(self, j, i)
                elif column == 'd':
                    Ground(self, j, i)
                    Diamond(self, j, i)
                elif column == 'p':
                    Ground(self, j, i)
                    Player(self, j, i)

    def play_music(self):
        pygame.mixer.music.load('../assets/theme.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(10)

    def randomize_objects(self, list, changes, object):
        # Cogemos los indices de los - en el mapa
        index = [i for i, x in enumerate([elem for sublist in list for elem in sublist]) if x == '-']

        # Se escogen los indices que se van a cambiar por el nuevo caracter
        selected_index = random.sample(index, changes)

        # Se crea la nueva lista cambiando los - elegidos por el caracter
        new_list_raw = [object if i in selected_index else x for i, x in
                        enumerate([elem for sublist in list for elem in sublist])]

        # Se reformatea la lista para dejarla como una lista de listas al igual que entró
        new_list = [new_list_raw[n:n + len(list[0])] for n in range(0, len(new_list_raw), len(list[0]))]

        return new_list
