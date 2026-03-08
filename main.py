import pygame
from config import *
from grid import create_grid, draw_grid, get_all_crops
from algorithms import astar

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Irrigation AI - A*")

font = pygame.font.SysFont("sans", 20)

grid = create_grid()
path = []

running = True
while running:

    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Reset grid
            if event.key == pygame.K_r:
                grid = create_grid()
                path = []

            # Run irrigation
            if event.key == pygame.K_a:

                start = None

                # Find water source
                for r in range(GRID_SIZE):
                    for c in range(GRID_SIZE):
                        if grid[r][c] == 2:
                            start = (r, c)

                # Get all crop tiles
                crops = get_all_crops(grid)

                current = start
                path = []

                # Visit crops sequentially
                for crop in crops:

                    full_path = astar(grid, current, crop)

                    if full_path:

                        for step in full_path:

                            path.append(step)

                            screen.fill(BACKGROUND_COLOR)
                            draw_grid(screen, grid, path)

                            # Water droplet animation
                            r, c = step
                            center = (
                                c * CELL_SIZE + CELL_SIZE // 2,
                                r * CELL_SIZE + CELL_SIZE // 2 + 50
                            )

                            pygame.draw.circle(screen, (0,150,255), center, 8)
                            pygame.draw.circle(screen,(200,230,255),center,3)

                            # UI text
                            title = font.render("Smart Irrigation System (A* Pathfinding)", True, (0,0,0))
                            screen.blit(title, (10, 10))

                            legend = font.render("Press A to Run A* | Press R to Reset", True, (0,0,0))
                            screen.blit(legend, (10, HEIGHT - 30))

                            pygame.display.update()

                            pygame.time.delay(120)

                    current = crop

    draw_grid(screen, grid, path)

    title = font.render("Smart Irrigation System (A* Pathfinding)", True, (0,0,0))
    screen.blit(title, (10, 10))

    legend = font.render("Press A to Run A* | Press R to Reset", True, (0,0,0))
    screen.blit(legend, (10, HEIGHT - 30))

    pygame.display.flip()

pygame.quit()