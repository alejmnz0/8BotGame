from model.Game import Game

game = Game()
game.new_game()
while game.playing:
    game.events()
    game.update()
    game.draw()
game.running = False
