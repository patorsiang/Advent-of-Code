def count_xmas_x_pattern(grid):
    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Check if a cell (r, c) is part of an "X-MAS" pattern
    def is_x_mas(r, c):
        # Check bounds for the cross structure
        if r < 1 or r >= rows - 1 or c < 1 or c >= cols - 1:
            return False
        # Possible "MAS" patterns
        mas_variants = ["MAS", "SAM"]
        # Check the X-MAS pattern
        top_left = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
        top_right = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]
        return top_left in mas_variants and top_right in mas_variants

    # Iterate through the grid
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_x_mas(r, c):
                count += 1

    return count


grid = list()

with open("input.txt", "r") as file:
  content = file.readlines()
  for line in content:
    grid.append(list(line.strip()))
# Count X-MAS patterns
result = count_xmas_x_pattern(grid)
print(f"Total occurrences of 'X-MAS': {result}")
