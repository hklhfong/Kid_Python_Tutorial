import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 1
BIRD_SPEED = -10
PIPE_SPEED = -5

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Initialize clock
clock = pygame.time.Clock()

# Bird properties
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_speed = 0

# Pipe properties
pipes = []
PIPE_WIDTH = 50
GAP_SIZE = 200

# Score
score = 0

def draw_bird(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, 40, 40))

def draw_pipe(x, height):
    pygame.draw.rect(screen, GREEN, (x, 0, PIPE_WIDTH, height))
    pygame.draw.rect(screen, GREEN, (x, height + GAP_SIZE, PIPE_WIDTH, SCREEN_HEIGHT - height - GAP_SIZE))

def check_collision():
    if bird_y < 0 or bird_y > SCREEN_HEIGHT:
        return True
    for pipe_x, pipe_height in pipes:
        if bird_x + 40 > pipe_x and bird_x < pipe_x + PIPE_WIDTH:
            if bird_y < pipe_height or bird_y + 40 > pipe_height + GAP_SIZE:
                return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = BIRD_SPEED

    # Update bird position
    bird_speed += GRAVITY
    bird_y += bird_speed

    # Generate pipes
    if len(pipes) == 0 or pipes[-1][0] < SCREEN_WIDTH - PIPE_WIDTH * 2:
        pipe_height = random.randint(50, SCREEN_HEIGHT - GAP_SIZE - 50)
        pipes.append((SCREEN_WIDTH, pipe_height))

    # Remove off-screen pipes
    if pipes[0][0] < -PIPE_WIDTH:
        pipes.pop(0)

    # Update pipe positions
    pipes = [(x + PIPE_SPEED, height) for x, height in pipes]

    # Check collision
    if check_collision():
        bird_x = 50
        bird_y = SCREEN_HEIGHT // 2
        bird_speed = 0
        pipes = []
        score = 0

    # Check for points
    if pipes and bird_x > pipes[0][0] + PIPE_WIDTH:
        pipes.pop(0)
        score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw pipes
    for pipe_x, pipe_height in pipes:
        draw_pipe(pipe_x, pipe_height)

    # Draw bird
    draw_bird(bird_x, bird_y)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(30)
