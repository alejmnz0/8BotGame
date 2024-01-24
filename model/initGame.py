import pygame

from model.Bot import Bot

robot = Bot()
pygame.init()


ventana = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("8BotGame")

jugando = True
while jugando:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            jugando = False

    ventana.fill((255, 255, 255))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
pygame.quit()
