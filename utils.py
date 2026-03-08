# utils.py

def get_neighbors(pos, grid):
    rows = len(grid)
    cols = len(grid[0])
    r, c = pos

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != 1:  # not obstacle
                neighbors.append((nr, nc))

    return neighbors