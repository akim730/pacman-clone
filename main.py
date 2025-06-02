import pygame
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 560, 620
FPS = 60
TILE_SIZE = 40

# Colors
BLACK = (0, 0, 0)
BLUE = (33, 33, 222)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pacman")
clock = pygame.time.Clock()

# Load images
pacman_img = pygame.transform.scale(pygame.image.load("assets/pacman.png"), (TILE_SIZE, TILE_SIZE))
wall_img = pygame.transform.scale(pygame.image.load("assets/wall.png"), (TILE_SIZE, TILE_SIZE))
pellet_img = pygame.transform.scale(pygame.image.load("assets/pellet.png"), (10, 10))

# Simple map
level = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "     #.##          ##.#     ",
    "     #.## ###--### ##.#     ",
    "######.## #      # ##.######",
    "      .   #      #   .      ",
    "######.## #      # ##.######",
    "     #.## ######## ##.#     ",
    "     #.##          ##.#     ",
    "     #.## ######## ##.#     ",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Pacman initial position
pacman_x, pacman_y = 13, 23
dx, dy = 0, 0
score = 0

def draw_world():
    global score
    for y, row in enumerate(level):
        for x, col in enumerate(row):
            if col == "#":
                screen.blit(wall_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif col == ".":
                screen.blit(pellet_img, (x * TILE_SIZE + 15, y * TILE_SIZE + 15))
            elif col == "o":
                pygame.draw.circle(screen, WHITE, (x * TILE_SIZE + 20, y * TILE_SIZE + 20), 8)

def update_pacman():
    global pacman_x, pacman_y, score
    next_x, next_y = pacman_x + dx, pacman_y + dy
    if level[next_y][next_x] != "#":
        if level[next_y][next_x] == ".":
            score += 10
            row = list(level[next_y])
            row[next_x] = " "
            level[next_y] = "".join(row)
        pacman_x, pacman_y = next_x, next_y

# Game loop
running = True
while running:
    screen.fill(BLACK)
    draw_world()
    screen.blit(pacman_img, (pacman_x * TILE_SIZE, pacman_y * TILE_SIZE))
    update_pacman()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: dx, dy = -1, 0
            if event.key == pygame.K_RIGHT: dx, dy = 1, 0
            if event.key == pygame.K_UP: dx, dy = 0, -1
            if event.key == pygame.K_DOWN: dx, dy = 0, 1

    pygame.display.set_caption(f"Mini Pacman | Score: {score}")
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

