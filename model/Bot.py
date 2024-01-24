import pygame


class Bot:
    hp = 10
    waterproof = False

    def __init__(self):
        self.position = [0, 0]
        self.speed = 10

    def move_right(self):
        self.position[0] += self.speed
