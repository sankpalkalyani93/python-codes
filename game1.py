import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
GRID_SIZE = 5
TILE_SIZE = 80

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WordScapes Simulator")
clock = pygame.time.Clock()

# Sample word list
word_list = ["CAT", "BAT", "RAT", "HAT", "MAT"]

# Function to generate a random grid of letters
def generate_grid():
    letters = [chr(random.randint(65, 90)) for _ in range(GRID_SIZE * GRID_SIZE)]
    random.shuffle(letters)
    grid = [letters[i:i+GRID_SIZE] for i in range(0, len(letters), GRID_SIZE)]
    return grid

# Function to draw the grid on the screen
def draw_grid(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, WHITE, (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            font = pygame.font.Font(None, 36)
            letter_text = font.render(grid[row][col], True, BLACK)
            screen.blit(letter_text, (col*TILE_SIZE + TILE_SIZE//2 - 15, row*TILE_SIZE + TILE_SIZE//2 - 15))

# Main game loop
grid = generate_grid()
selected_tiles = []
current_word = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = y // TILE_SIZE
            selected_tiles.append((row, col))
            current_word += grid[row][col]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if current_word in word_list:
                    print("Valid word:", current_word)
                    # Logic for correct word
                else:
                    print("Invalid word:", current_word)
                    # Logic for incorrect word
                selected_tiles = []
                current_word = ""

    screen.fill(BLACK)
    draw_grid(grid)

    # Highlight selected tiles
    for row, col in selected_tiles:
        pygame.draw.rect(screen, (0, 128, 255), (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE), 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
