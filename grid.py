import pygame
import random
from config import *

# Load images once
water_img = pygame.image.load("assets/water.png")
crop_img = pygame.image.load("assets/crop.png")
rock_img = pygame.image.load("assets/rock.png")

water_img = pygame.transform.scale(water_img, (CELL_SIZE-10, CELL_SIZE-10))
crop_img = pygame.transform.scale(crop_img, (CELL_SIZE, CELL_SIZE))
bigger_crop_img = pygame.transform.scale(crop_img, (CELL_SIZE-12, CELL_SIZE-12))
rock_img = pygame.transform.scale(rock_img, (CELL_SIZE, CELL_SIZE))


# 🌱 Create crop clusters
def place_crop_cluster(grid, size=2):

    r = random.randint(1, GRID_SIZE - size - 1)
    c = random.randint(1, GRID_SIZE - size - 1)

    for i in range(size):
        for j in range(size):

            if grid[r+i][c+j] == 0:
                grid[r+i][c+j] = 3
# 🌾 Create grid
def create_grid():

    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Water source
    grid[0][0] = 2

    # Generate crop groups
    for _ in range(3):
        place_crop_cluster(grid, size=2)

    # Random obstacles
    for _ in range(15):

        r = random.randint(0, GRID_SIZE - 1)
        c = random.randint(0, GRID_SIZE - 1)

        if grid[r][c] == 0:
            grid[r][c] = 1

    return grid


# 🌱 Get all crop coordinates
def get_all_crops(grid):

    crops = []

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):

            if grid[r][c] == 3:
                crops.append((r, c))

    return crops


# 🎨 Draw grid
def draw_grid(screen, grid, path=None):

    if path is None:
        path = []

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):

            rect = pygame.Rect(
                c * CELL_SIZE,
                r * CELL_SIZE + 50,
                CELL_SIZE,
                CELL_SIZE
            )

            # Base ground
            pygame.draw.rect(screen, EMPTY_COLOR, rect)

            # Obstacles
            if grid[r][c] == 1:
                screen.blit(rock_img, rect)

            # Water source
            elif grid[r][c] == 2:
                screen.blit(water_img, rect.inflate(-10, -10))

            # Crops
            elif grid[r][c] == 3:

                pygame.draw.rect(screen, (190,255,190), rect)

                if (r, c) in path:
                    screen.blit(bigger_crop_img, rect.inflate(-12, -12))
                else:
                    screen.blit(crop_img, rect.inflate(-12, -12))

            # Irrigation path
            if (r, c) in path:
                overlay = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                overlay.fill((120,180,255,140))
                screen.blit(overlay, rect)

            # Grid lines
            pygame.draw.rect(screen, GRID_LINE_COLOR, rect, 1)