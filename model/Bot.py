class Bot:
    def __init__(self, sprite):
        self.position = [0, 0]
        self.speed = 2
        self.hp = 10
        self.sprite = sprite
        self.size = [100, 100]

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed
