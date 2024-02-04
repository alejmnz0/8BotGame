from model.Item import Item


class Diamond(Item):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.objects_spritesheet.get_sprite(0, 0, self.width, self.height)
