# Your Python code (GameCenter) up to the 'main_menu' function...

class GameCenterApp(App):
    def build(self):
        return Builder.load_file("gamecenter.kv")

    def load_game(self, game_name):
        if game_name == 'snake':
            # Load and start the Snake game
            snake_game = SnakeGame()
            snake_game.start_game()
        elif game_name == 'tic_tac_toe':
            # Load and start the Tic Tac Toe game
            tic_tac_toe_game = TicTacToeGame()
            tic_tac_toe_game.start_game()
        elif game_name == 'pong':
            # Load and start the Pong game
            pong_game = PongGame()
            pong_game.start_game()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    GameCenterApp().run()
