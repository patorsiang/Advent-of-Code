# Helper functions for flood fill (DFS) to calculate area and perimeter
def calculate_region_properties(grid, x, y, visited):
    """Flood-fill to calculate the area and perimeter of a region."""
    stack = [(x, y)]
    visited[x][y] = True
    plant_type = grid[x][y]
    area = 0
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cx, cy = stack.pop()
        area += 1
        for dx, dy in directions:
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

# Main computation for all regions
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

with open('input.txt', 'r') as f:
   garden_map = [list(line.strip()) for line in f]

print(compute_total_fencing_cost(garden_map))
