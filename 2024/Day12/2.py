import sys
from collections import deque

# Directions for up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def calculate_region_properties(grid, x, y, visited):
    """Flood-fill to calculate the area and perimeter of a region."""
    stack = [(x, y)]
    visited[x][y] = True
    plant_type = grid[x][y]
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        area += 1
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == plant_type and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter

def compute_total_fencing_cost(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_cost = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:  # Found a new region
                area, perimeter = calculate_region_properties(grid, i, j, visited)
                total_cost += area * perimeter

    return total_cost

def compute_total_side_cost(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_cost = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:  # Found a new region
                stack = [(i, j)]
                visited[i][j] = True
                plant_type = grid[i][j]
                area = 0
                sides = 0

                # To track visited boundary cells for side calculation
                boundary_visited = set()

                while stack:
                    cx, cy = stack.pop()
                    area += 1
                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if grid[nx][ny] == plant_type and not visited[nx][ny]:
                                stack.append((nx, ny))
                                visited[nx][ny] = True
                            elif grid[nx][ny] != plant_type:
                                if (cx, cy) not in boundary_visited:
                                    sides += 1
                                    boundary_visited.add((cx, cy))
                        else:
                            if (cx, cy) not in boundary_visited:
                                sides += 1
                                boundary_visited.add((cx, cy))

                total_cost += area * sides

    return total_cost

with open('input.txt', 'r') as f:
    garden_map = [list(line.strip()) for line in f]

print("Total fencing cost (perimeter):", compute_total_fencing_cost(garden_map))
print("Total fencing cost (sides):", compute_total_side_cost(garden_map))
