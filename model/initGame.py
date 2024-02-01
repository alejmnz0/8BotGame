import enviroment
from model.Game import Game

tilemap1 = open(enviroment.file).read().split("\n")
tilemap2 = []
for x in tilemap1:
    tilemap2.append(x.split(','))

game = Game()
game.new_game(tilemap2)
while game.playing:
    game.events()
    game.update()
    game.draw()
game.running = False
