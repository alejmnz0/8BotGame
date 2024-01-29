import pygame
import enviroment
import Wall
from model.Game import Game

pygame.init()
sprite = pygame.image.load(enviroment.character)
ventana = pygame.display.set_mode((enviroment.width, enviroment.height))
tilemap1 = open(enviroment.file).read().split("\n")
tilemap2 = []
for x in tilemap1:
    tilemap2.append(x.split(','))


def createTilemap(self):
    for i, row in enumerate(tilemap2):
        for j, column in enumerate(row):
            if column == 'b':
                Wall.Wall(j, i)


game = Game()
game.new_game()
while game.playing:
    game.events()
    game.update()
    game.draw()
game.running = False

# pygame.display.set_caption("8BotGame")
# font = pygame.font.Font(None, 50)
#
# jugando = True
# while jugando:
#     createTilemap(tilemap2)
#     ventana.blit(robot.sprite, robot.position)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             match event.key:
#                 case pygame.K_d:
#                     robot.move_right()
#                 case pygame.K_a:
#                     robot.move_left()
#                 case pygame.K_w:
#                     robot.move_up()
#                 case pygame.K_s:
#                     robot.move_down()
#         if event.type == pygame.QUIT:
#             jugando = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_d]:
#         robot.move_right()
#     if keys[pygame.K_a]:
#         robot.move_left()
#     if keys[pygame.K_w]:
#         robot.move_up()
#     if keys[pygame.K_s]:
#         robot.move_down()
#
#     pygame.display.flip()
#
#     pygame.time.Clock().tick(60)
# pygame.quit()
