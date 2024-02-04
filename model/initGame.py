from model.Game import Game

game = Game()
game.show_intro_screen()
game.new_game()
while game.running:
    game.play()
    game.show_game_over()
