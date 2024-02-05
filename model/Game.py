import random

import pygame
import enviroment
from model.Cracked import Cracked
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
        self.font = pygame.font.Font(enviroment.font, enviroment.font_size)
        self.character_spritesheet = Spritesheet(enviroment.character_sprites)
        self.dive_spritesheet = Spritesheet(enviroment.dive_sprites)
        self.terrain_spritesheet = Spritesheet(enviroment.terrain_sprites)
        self.objects_spritesheet = Spritesheet(enviroment.objects_sprites)
        self.intro_background = pygame.image.load(enviroment.background_image)
        self.game_over_background = pygame.image.load(enviroment.gameover_image)
        self.menu_background = pygame.image.load(enviroment.menu_image)

    def play(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def new_game(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.threats = pygame.sprite.LayeredUpdates()
        self.breakable_objects = pygame.sprite.LayeredUpdates()
        self.create_map()
        self.play_music()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu_screen()
            if event.type == pygame.QUIT:
                self.show_menu_screen()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(enviroment.black)
        self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                hp_info = self.font.render(f' Hp: {sprite.hp}', True, enviroment.white)
                self.screen.blit(hp_info, (0, 905))

                bombs_info = self.font.render(f'{sprite.bombs}', True, enviroment.white)
                self.screen.blit(bombs_info, (275, 905))
                self.screen.blit(pygame.transform.scale(
                    self.objects_spritesheet.get_sprite(50, 0, enviroment.tilesize, enviroment.tilesize), (40, 40)),
                    (225, 905))

                points_info = self.font.render(f'{sprite.points}', True, enviroment.white)
                self.screen.blit(points_info, (500, 905))
                self.screen.blit(pygame.transform.scale(
                    self.objects_spritesheet.get_sprite(0, 0, enviroment.tilesize, enviroment.tilesize), (40, 40)),
                                 (450, 905))

                if sprite.dive_suit:
                    self.screen.blit(pygame.transform.scale(
                        self.objects_spritesheet.get_sprite(25, 0, enviroment.tilesize, enviroment.tilesize), (40, 40)),
                        (360, 905))
                else:
                    self.screen.blit(pygame.transform.scale(
                        self.objects_spritesheet.get_sprite(100, 0, enviroment.tilesize, enviroment.tilesize), (40, 40)),
                        (360, 905))

        self.clock.tick(enviroment.fps)
        pygame.display.update()

    def create_map(self):
        tilemap1 = open(enviroment.file).read().split("\n")
        tilemap2 = []
        for x in tilemap1:
            tilemap2.append(x.split(','))

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
                elif column == 'k':
                    Ground(self, j, i)
                    Cracked(self, j, i)

    def play_music(self):
        pygame.mixer.music.load(enviroment.music_theme)
        pygame.mixer.music.set_volume(0.1)
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

    def show_game_over(self):
        text = self.font.render('Game Over', True, enviroment.black)
        subtext = self.font.render('Pres SPACE to restart', True, enviroment.black)
        subtext2 = self.font.render('Pres ESC to exit', True, enviroment.black)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.new_game()
                        self.play()
            self.screen.blit(self.game_over_background, (0, 0))
            self.screen.blit(text, (650, 200))
            self.screen.blit(subtext, (500, 300))
            self.screen.blit(subtext2, (500, 400))
            self.clock.tick(enviroment.fps)
            pygame.display.update()

    def show_intro_screen(self):
        intro = True
        title = self.font.render('8BitGame', True, enviroment.black)
        subtitle = self.font.render('Press SPACE to play', True, enviroment.black)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro = False
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, (650, 200))
            self.screen.blit(subtitle, (500, 300))
            self.clock.tick(enviroment.fps)
            pygame.display.update()

    def show_menu_screen(self):
        confirm = True
        text = self.font.render('Are you sure?', True, enviroment.white)
        subtext = self.font.render('Pres SPACE to resume', True, enviroment.white)
        subtext2 = self.font.render('Pres ESC to exit', True, enviroment.white)

        while confirm:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    confirm = False
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        confirm = False
                        self.playing = True
                        self.running = True
                    if event.key == pygame.K_ESCAPE:
                        confirm = False
                        self.playing = False
                        self.running = False
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(text, (650, 200))
            self.screen.blit(subtext, (550, 300))
            self.screen.blit(subtext2, (550, 400))
            self.clock.tick(enviroment.fps)
            pygame.display.update()
