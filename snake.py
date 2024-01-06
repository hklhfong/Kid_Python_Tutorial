import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 15
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
GREEN = (0, 50, 0)
SNAKE = (random.randint(150, 255),random.randint(150, 255),random.randint(150, 255))
APPLE = (255, 0, 0)

# Direction (0: up, 1: right, 2: down, 3: left)
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = RIGHT

# Initialize food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game over flag
game_over = False

# Flag to start the game when any key is pressed
start_game = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                start_game = True
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
            else:
                # Start the game when any key is pressed after a game over
                game_over = False
                

    if not game_over and start_game:
        # Move the snake
        head_x, head_y = snake[0]
        if snake_direction == UP:
            new_head = (head_x, head_y - 1)
        elif snake_direction == RIGHT:
            new_head = (head_x + 1, head_y)
        elif snake_direction == DOWN:
            new_head = (head_x, head_y + 1)
        elif snake_direction == LEFT:
            new_head = (head_x - 1, head_y)

        # Check for collisions
        if new_head == food:
            # Snake eats the food
            snake.insert(0, new_head)
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        elif new_head in snake or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            # Game over conditions
            game_over = True
        else:
            # Move the snake
            snake.insert(0, new_head)
            snake.pop()

        # Clear the screen
        screen.fill(GREEN)


    if not start_game:
        font = pygame.font.Font(None, 36)
        text = font.render("Press any key to start", True, SNAKE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
    else:
        # Draw food
        pygame.draw.rect(screen, APPLE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, SNAKE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
