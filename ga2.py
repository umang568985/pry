import random
import pygame
import sys
import math
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",180)

def main_menu():
        while True:
            engine.say("Welcome to the Game Center!")
            engine.say("Please select a game:")
            engine.say("one. Snake")
            engine.say("two. Tic Tac Toe")
            engine.say("Three. pong")
            engine.runAndWait()
            
   

            print("Welcome to the Game Center!")
            print("1. Snake")
            print("2. Tic Tac Toe")
            print("3. pong")
            print("4. Quit")
            
            choice = input("Select a game (1-4): ")
            
            if choice == '1':
                # Start snake game
                engine.say("Welcome to Snake. Let's play!")
                engine.runAndWait()
                import pygame
                import random
                import numpy as np

                # Initialize Pygame
                pygame.init()

                # Constants
                WIDTH, HEIGHT = 640, 480
                GRID_SIZE = 20
                GRID_WIDTH = WIDTH // GRID_SIZE
                GRID_HEIGHT = HEIGHT // GRID_SIZE

                # Colors
                LIGHT_BLUE = (173, 216, 230)
                DARK_COLOR = (50, 50, 50)
                GREEN = (0, 255, 0)
                RED = (255, 0, 0)
                DARK_SNAKE_COLOR = (0, 0, 0)
                WHITE = (255, 255, 255)
                HIGHLIGHT = (255, 255, 0)

                # Function to generate a simple beep sound
                def generate_beep(frequency, duration_ms):
                    sample_rate = 44100  # Sample rate (samples per second)
                    num_samples = int((duration_ms / 1000.0) * sample_rate)
                    audio_data = np.array([32767.0 * 0.5 * np.sin(2 * np.pi * frequency * t / sample_rate) for t in range(num_samples)])
                    return audio_data.astype(np.int16)

                # Function to play the beep sound
                def play_beep():
                    beep_sound = pygame.mixer.Sound(generate_beep(800, 100))  # Generate and play a beep sound
                    beep_sound.play()

                # Initialize the screen
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Snake Game")

                # Initialize the clock
                clock = pygame.time.Clock()

                # Snake initial position
                snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                snake_direction = (1, 0)

                # Food initial position
                food = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))

                # Game variables
                score = 0
                game_over = False

                # Circles representing the snake's body
                snake_body = [(snake[0][0], snake[0][1])]

                # Function to generate new food position
                def generate_food():
                    while True:
                        new_food = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
                        if new_food not in snake_body:
                            return new_food

                # Font for displaying the score
                font = pygame.font.Font(None, 36)

                # Main game loop
                while True:
                    while not game_over:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP and snake_direction != (0, 1):
                                    snake_direction = (0, -1)
                                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                                    snake_direction = (0, 1)
                                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                                    snake_direction = (-1, 0)
                                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                                    snake_direction = (1, 0)

                        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

                        if (
                            new_head[0] < 1
                            or new_head[0] >= GRID_WIDTH - 1
                            or new_head[1] < 1
                            or new_head[1] >= GRID_HEIGHT - 1
                            or new_head in snake_body
                        ):
                            game_over = True
                            play_beep() 
                        else:
                            snake.insert(0, new_head)

                        if snake[0] == food:
                            score += 10
                            food = generate_food()
                            play_beep()
                        else:
                            snake_body.pop()

                        snake_body.insert(0, (new_head[0], new_head[1]))

                        if len(snake_body) > score + 1:
                            snake_body.pop()

                        screen.fill(LIGHT_BLUE)
                        pygame.draw.rect(screen, DARK_COLOR, (0, 0, WIDTH, GRID_SIZE))
                        pygame.draw.rect(screen, DARK_COLOR, (0, 0, GRID_SIZE, HEIGHT))
                        pygame.draw.rect(screen, DARK_COLOR, (0, HEIGHT - GRID_SIZE, WIDTH, GRID_SIZE))
                        pygame.draw.rect(screen, DARK_COLOR, (WIDTH - GRID_SIZE, 0, GRID_SIZE, HEIGHT))

                        for i, segment in enumerate(snake_body):
                            if i == 0:
                                pygame.draw.circle(screen, DARK_SNAKE_COLOR, (segment[0] * GRID_SIZE + GRID_SIZE // 2, segment[1] * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)
                            else:
                                pygame.draw.circle(screen, DARK_SNAKE_COLOR, (segment[0] * GRID_SIZE + GRID_SIZE // 2, segment[1] * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)

                        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

                        score_text = font.render(f"Score: {score}", True, WHITE)
                        score_rect = score_text.get_rect(center=(WIDTH // 2, GRID_SIZE // 2))
                        pygame.draw.rect(screen, HIGHLIGHT, (score_rect.left - 5, score_rect.top - 5, score_rect.width + 10, score_rect.height + 10))
                        screen.blit(score_text, score_rect)

                        pygame.display.flip()
                        clock.tick(10)

                    screen.fill(LIGHT_BLUE)
                    
                    game_over_font = pygame.font.Font(None, 72)
                    game_over_text = game_over_font.render("Game Over", True, DARK_COLOR)
                    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
                    screen.blit(game_over_text, game_over_rect)

                    final_score_text = font.render(f"Your Score: {score}", True, DARK_COLOR)
                    final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
                    screen.blit(final_score_text, final_score_rect)

                    play_again_text = font.render("Press 'P' to Play Again or 'Q' to Quit", True, DARK_COLOR)
                    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
                    screen.blit(play_again_text, play_again_rect)

                    pygame.display.flip()

                    wait_for_input = True
                    while wait_for_input:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    game_over = False
                                    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                                    snake_direction = (1, 0)
                                    food = generate_food()
                                    score = 0
                                    snake_body = [(snake[0][0], snake[0][1])]
                                    wait_for_input = False
                                elif event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()

                    clock.tick(5)

                pygame.quit()

                pass

            elif choice == '2':
                # Start Tic Tac Toe game
                engine.say("Welcome to tic tac tow. Let's play!")
                engine.runAndWait()
                import pygame
                import random
                import sys
                import numpy as np

                # Initialize Pygame
                pygame.init()

                # Constants
                WIDTH, HEIGHT = 600, 600
                GRID_SIZE = 200
                LINE_WIDTH = 10

                # Define custom RGB color variables for the background
                Background_color = (135, 206, 235)  # Sky Blue color
                Black_color = (0, 0, 0)

                # Function to generate a simple beep sound
                def generate_beep(frequency, duration_ms):
                    sample_rate = 44100  # Sample rate (samples per second)
                    num_samples = int((duration_ms / 1000.0) * sample_rate)
                    audio_data = np.array([32767.0 * 0.5 * np.sin(2 * np.pi * frequency * t / sample_rate) for t in range(num_samples)])
                    return audio_data.astype(np.int16)

                # Function to play the beep sound
                def play_beep():
                    beep_sound = pygame.mixer.Sound(generate_beep(800, 100))  # Generate and play a beep sound
                    beep_sound.play()

                # Font size for the symbols
                SYMBOL_FONT_SIZE = 200  # Adjust the font size for the symbols
                MESSAGE_FONT_SIZE = 40

                # Initialize the board
                board = [[" " for _ in range(3)] for _ in range(3)]

                # Create a font object for the symbols
                symbol_font = pygame.font.Font(None, SYMBOL_FONT_SIZE)

                # Create a font object for messages
                message_font = pygame.font.Font(None, MESSAGE_FONT_SIZE)

                # Get Player Names
                player1_name = input("Enter Player 1's name: ")
                player2_name = input("Enter Player 2's name: ")

                current_player = "X"
                winner = None

                # Initialize the screen
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Tic-Tac-Toe")

                # Function to draw the board
                def draw_board():
                    screen.fill(Background_color)  # Clear the screen

                    for i in range(1, 3):
                        pygame.draw.rect(screen, Black_color, (i * GRID_SIZE - LINE_WIDTH // 2, 0, LINE_WIDTH, HEIGHT))
                        pygame.draw.rect(screen, Black_color, (0, i * GRID_SIZE - LINE_WIDTH // 2, WIDTH, LINE_WIDTH))

                    for row in range(3):
                        for col in range(3):
                            left = col * GRID_SIZE
                            top = row * GRID_SIZE
                            symbol_text = symbol_font.render(board[row][col], True, Black_color)  # Use the symbol font
                            symbol_rect = symbol_text.get_rect(center=(left + GRID_SIZE / 2, top + GRID_SIZE / 2))
                            screen.blit(symbol_text, symbol_rect)

                # Function to check for a win
                def check_winner():
                    for row in board:
                        if all(cell == current_player for cell in row):
                            return True

                    for col in range(3):
                        if all(board[row][col] == current_player for row in range(3)):
                            return True

                    if all(board[i][i] == current_player for i in range(3)) or all(board[i][2 - i] == current_player for i in range(3)):
                        return True

                    return False

                # Function to check for a draw
                def check_draw():
                    return all(cell != " " for row in board for cell in row) and winner is None

                # Function to draw the game over screen
                def draw_game_over():
                    pygame.draw.rect(screen, Background_color, (100, HEIGHT // 2 - 50, WIDTH - 200, 100))
                    message = f"{player1_name if winner == 'X' else player2_name} wins!"
                    if winner == "Draw":
                        message = "It's a draw!"
                    message_text = message_font.render(message, True, Black_color)  # Use the message font
                    message_rect = message_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                    screen.blit(message_text, message_rect)
                    pygame.display.flip()

                    pygame.draw.rect(screen, Background_color, (150, HEIGHT // 2 + 60, WIDTH - 300, 100))
                    play_again_text = message_font.render("Play Again (click here)", True, Black_color)  # Use the message font
                    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 110))
                    screen.blit(play_again_text, play_again_rect)

                    quit_text = message_font.render("Quit (click here)", True, Black_color)  # Use the message font
                    quit_rect = quit_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 210))
                    screen.blit(quit_text, quit_rect)

                    pygame.display.flip()

                # Main game loop
                playing = True
                play_again = True  # Initialize the play again flag

                while playing:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            playing = False

                        if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                            x, y = event.pos
                            row = y // GRID_SIZE
                            col = x // GRID_SIZE
                            if board[row][col] == " ":
                                board[row][col] = current_player
                                play_beep()
                                if check_winner():
                                    winner = current_player
                                elif check_draw():
                                    winner = "Draw"
                                else:
                                    current_player = "O" if current_player == "X" else "X"

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                            playing = False
                            play_again = False

                    draw_board()
                    pygame.display.flip()

                    if winner:
                        draw_game_over()

                        waiting_for_response = True

                        while waiting_for_response:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x, y = event.pos
                                    if 150 <= x <= WIDTH - 150 and HEIGHT // 2 + 60 <= y <= HEIGHT // 2 + 160:
                                        board = [[" " for _ in range(3)] for _ in range(3)]
                                        current_player = "X"
                                        winner = None
                                        waiting_for_response = False

                                    elif 150 <= x <= WIDTH - 150 and HEIGHT // 2 + 210 <= y <= HEIGHT // 2 + 310:
                                        waiting_for_response = False
                                        play_again = False
                                        playing = False

                # Ask if the players want to play again
                if play_again:
                    print("Play again")
                else:
                    print("Quit")

                pygame.quit()
                sys.exit()
                pass
            elif choice == '3':
                # Start pong
                engine.say("Welcome to pong. Let's play!")
                engine.runAndWait()
                import pygame
                import random
                import sys
                import numpy as np

                # Initialize Pygame
                pygame.init()

                # Constants
                WIDTH, HEIGHT = 800, 600
                BALL_RADIUS = 20
                PADDLE_WIDTH = 10
                PADDLE_HEIGHT = 100
                BALL_SPEED = 4
                PADDLE_SPEED = 4
                WIN_SCORE = 11

                # Colors
                WHITE = (255, 255, 255)
                LIGHT_BLUE = (173, 216, 230)
                DARK_BLUE = (0, 0, 139)
                DARK_BLACK = (0, 0, 0)
                PADDLE_COLOR = DARK_BLACK
                BALL_COLOR = DARK_BLACK

                # Function to generate a simple beep sound
                def generate_beep(frequency, duration_ms):
                    sample_rate = 44100  # Sample rate (samples per second)
                    num_samples = int((duration_ms / 1000.0) * sample_rate)
                    audio_data = np.array([32767.0 * 0.5 * np.sin(2 * np.pi * frequency * t / sample_rate) for t in range(num_samples)])
                    return audio_data.astype(np.int16)

                # Function to play the beep sound
                def play_beep():
                    beep_sound = pygame.mixer.Sound(generate_beep(800, 100))  # Generate and play a beep sound
                    beep_sound.play()

                # Create the game window
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Pong Game")

                # Initialize the clock
                clock = pygame.time.Clock()

                # Initialize paddles and ball
                player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
                opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
                ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

                ball_speed_x = BALL_SPEED * random.choice((1, -1))
                ball_speed_y = BALL_SPEED * random.choice((1, -1))

                player_paddle_speed = 0
                opponent_paddle_speed = 0

                # Score variables
                player_score = 0
                opponent_score = 0
                font = pygame.font.Font(None, 36)

                # Game state
                game_over = False
                winner = None

                # Main game loop
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if not game_over:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    player_paddle_speed = -PADDLE_SPEED
                                if event.key == pygame.K_DOWN:
                                    player_paddle_speed = PADDLE_SPEED
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    player_paddle_speed = 0

                    if not game_over:
                        # Update opponent's paddle position (controlled automatically)
                        if ball.y > opponent_paddle.y + opponent_paddle.height // 2:
                            opponent_paddle_speed = PADDLE_SPEED - 1  # Reduced opponent speed
                        else:
                            opponent_paddle_speed = -PADDLE_SPEED + 1  # Reduced opponent speed

                        opponent_paddle.y += opponent_paddle_speed

                        # Ensure the opponent's paddle stays within the screen
                        opponent_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, opponent_paddle.y))

                        # Update paddle positions
                        player_paddle.y += player_paddle_speed

                        # Ensure the player's paddle stays within the screen
                        player_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, player_paddle.y))

                        # Update ball position
                        ball.x += ball_speed_x
                        ball.y += ball_speed_y

                        # Ball collisions with top and bottom walls
                        if ball.top <= 0 or ball.bottom >= HEIGHT:
                            ball_speed_y = -ball_speed_y
                            play_beep()  # Play beep sound on collision

                        # Ball collisions with paddles
                        if ball.colliderect(player_paddle):
                            ball_speed_x = abs(ball_speed_x)
                            play_beep()  # Play beep sound on collision

                        if ball.colliderect(opponent_paddle):
                            ball_speed_x = -abs(ball_speed_x)
                            play_beep()  # Play beep sound on collision

                        # Ball out of bounds
                        if ball.left <= 0:
                            # Opponent scores a point
                            opponent_score += 1
                            if opponent_score >= WIN_SCORE:
                                game_over = True
                                winner = "Opponent"
                            ball.topleft = (WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2)
                            ball_speed_x = BALL_SPEED * random.choice((1, -1))
                            ball_speed_y = BALL_SPEED * random.choice((1, -1))

                        if ball.right >= WIDTH:
                            # Player scores a point
                            player_score += 1
                            if player_score >= WIN_SCORE:
                                game_over = True
                                winner = "Player"
                            ball.topleft = (WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2)
                            ball_speed_x = BALL_SPEED * random.choice((1, -1))
                            ball_speed_y = BALL_SPEED * random.choice((1, -1))

                    # Clear the screen
                    screen.fill(LIGHT_BLUE)

                    # Draw boundaries
                    pygame.draw.rect(screen, DARK_BLUE, (0, 0, WIDTH, 5))
                    pygame.draw.rect(screen, DARK_BLUE, (0, HEIGHT - 5, WIDTH, 5))
                    pygame.draw.rect(screen, DARK_BLUE, (0, 0, 5, HEIGHT))
                    pygame.draw.rect(screen, DARK_BLUE, (WIDTH - 5, 0, 5, HEIGHT))

                    # Draw paddles and ball
                    pygame.draw.rect(screen, PADDLE_COLOR, player_paddle)
                    pygame.draw.rect(screen, PADDLE_COLOR, opponent_paddle)
                    pygame.draw.ellipse(screen, BALL_COLOR, ball)

                    if game_over:
                        # Display game over message with the winner
                        game_over_text = font.render(f"Game Over - {winner} Wins!", True, WHITE)
                        restart_text = font.render("Press R to play again or Q to quit", True, WHITE)
                        screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 20))
                        screen.blit(restart_text, (WIDTH // 2 - 190, HEIGHT // 2 + 40))

                    else:
                        # Draw scores
                        player_text = font.render(f"Player: {player_score}", True, WHITE)
                        opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
                        screen.blit(player_text, (10, 10))
                        screen.blit(opponent_text, (WIDTH - 200, 10))

                    # Update the display
                    pygame.display.update()

                    # Check for restart or quit
                    keys = pygame.key.get_pressed()
                    if game_over:
                        if keys[pygame.K_r]:
                            player_score = 0
                            opponent_score = 0
                            game_over = False
                            winner = None
                            player_paddle.topleft = (50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
                            opponent_paddle.topleft = (WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
                            ball.topleft = (WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2)
                            ball_speed_x = BALL_SPEED * random.choice((1, -1))
                            ball_speed_y = BALL_SPEED * random.choice((1, -1))

                        elif keys[pygame.K_q]:
                            pygame.quit()
                            sys.exit()

                    # Control game speed
                    clock.tick(60)

            pass
        
        else:
            print("Invalid choice. Please select a valid option.")

#if __name__ == "__main__":
main_menu()
