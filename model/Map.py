import pygame.image
import enviroment


class Map:

    def build_map(self, screen):
        tilemap = open(enviroment.file).readlines()
        walls = []
        x = 0
        y = 0
        for row in tilemap:
            for wall in row:
                if wall == 'b':
                    screen.blit(pygame.image.load(enviroment.wall_image), (x, y))
                    walls.append(pygame.image.load(enviroment.wall_image))
                    x += 25
                elif wall == '-':
                    screen.blit(pygame.image.load(enviroment.ground_image), (x, y))
                    walls.append(pygame.image.load(enviroment.ground_image))
                    x += 25
            x = 0
            y += 25
