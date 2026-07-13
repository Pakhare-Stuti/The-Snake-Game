import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

# --- Configuration ---
BLOCK_SIZE = 10  # size of one “cell” in px
GRID_WIDTH = 64  # number of cells horizontally
GRID_HEIGHT = 48  # number of cells vertically
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
SNAKE_SPEED = 15  # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake (Wrap‐around)")

# --- Game state ---
snake_pos = [GRID_WIDTH // 2 * BLOCK_SIZE, GRID_HEIGHT // 2 * BLOCK_SIZE]
snake_body = [
    [snake_pos[0], snake_pos[1]],
    [snake_pos[0] - BLOCK_SIZE, snake_pos[1]],
    [snake_pos[0] - 2 * BLOCK_SIZE, snake_pos[1]]
]
direction = 'RIGHT'
change_to = direction

# Food spawning on 10‐pixel grid
food_pos = [
    random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE),
    random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
]
food_spawn = True
score = 0

font = pygame.font.Font(None, 24)

def show_score():
    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (10, 10))

def game_over():
    msg = font.render(f"Game over! Score: {score}", True, RED)
    rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(msg, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# --- Main loop ---
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                change_to = 'UP'
            elif e.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif e.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif e.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent snake reversing directly
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    # Wrap‐around at edges (teleport to other side) †StackOverflow recommendation
    snake_pos[0] %= SCREEN_WIDTH
    snake_pos[1] %= SCREEN_HEIGHT

    snake_body.insert(0, list(snake_pos))

    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        # Spawn food at a new random cell
        food_pos = [
            random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE),
            random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        ]
        food_spawn = True

    # Draw
    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    show_score()

    # Self‐collision check — only game‐over condition now
    for body_block in snake_body[1:]:
        if body_block == snake_pos:
            game_over()

    pygame.display.update()

    clock.tick(SNAKE_SPEED)
