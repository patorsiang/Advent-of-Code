# Load the map from the uploaded file
file_path = "small_input.txt"

# Read the grid
with open(file_path, "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Get the dimensions of the grid
rows, cols = len(grid), len(grid[0])

def start_pos(grid):
  direction = ""
  for r in range(rows):
    for c in range(cols):
      match grid[r][c]:
        case '^':
          direction = "up"
        case '>':
          direction = "right"
        case 'v':
          direction = "down"
        case '<':
          direction = "left"
        case _:
          continue
      if direction != "":
        return r, c, direction

def move_pos(r, c, direct):
  new_r = r
  new_c = c
  direction = ['up', 'right', 'down', 'left']
  while grid[new_r][new_c] != '#' and new_r > 0 and new_c > 0 and new_c < rows -1 and new_r < cols-1:
    match direct:
      case "up":
        new_r -= 1
      case "right":
        new_c += 1
      case "down":
        new_r += 1
      case "left":
        new_c -= 1
      case _:
        raise ValueError("Invalid direction")

    if grid[new_r][new_c] != '#':
      r = new_r
      c = new_c
      grid[new_r][new_c] = 'X'
    else:
      direct = direction[direction.index(direct) + 1 if direction.index(direct) < len(direction) - 1 else 0]
      new_r = r
      new_c = c

  return r, c, direct



start_row, start_col, start_direct = start_pos(grid)
print(start_row, start_col, start_direct)
print(move_pos(start_row, start_col, start_direct))

def count_x(grid):
  return sum(row.count('X') for row in grid)

print(count_x(grid))

with open('small_output.txt', 'w') as file:
  for row in grid:
    file.write(''.join(row) + '\n')
