def count_xmas(grid, word="XMAS"):
    # Get dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Left
        (-1, 0), # Up
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def match(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if not in_bounds(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if match(r, c, dr, dc):
                    count += 1
    return count

grid = list()

with open("input.txt", "r") as file:
  content = file.readlines()
  for line in content:
    grid.append(list(line.strip()))

# Count occurrences of "XMAS"
result = count_xmas(grid)
print(f"Total occurrences of 'XMAS': {result}")
