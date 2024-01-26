import pygame

from model.Bot import Bot

pygame.init()
sprite = pygame.image.load("../assets/default.png")
robot = Bot(sprite)

ventana = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("8BotGame")
font = pygame.font.Font(None, 50)

jugando = True
while jugando:
    ventana.fill((255, 255, 255))
    ventana.blit(robot.sprite, robot.position)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_d:
                    robot.move_right()
                case pygame.K_a:
                    robot.move_left()
                case pygame.K_w:
                    robot.move_up()
                case pygame.K_s:
                    robot.move_down()
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        robot.move_right()
    if keys[pygame.K_a]:
        robot.move_left()
    if keys[pygame.K_w]:
        robot.move_up()
    if keys[pygame.K_s]:
        robot.move_down()


    pygame.display.flip()

    pygame.time.Clock().tick(60)
pygame.quit()
