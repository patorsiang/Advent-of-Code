from collections import deque
import itertools

def parse_input(grid):
    guard_pos = None
    guard_dir = None
    obstacles = set()
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char in directions:
                guard_pos = (x, y)
                guard_dir = char

    return guard_pos, guard_dir, obstacles

def next_position(position, direction):
    x, y = position
    dx, dy = direction
    return x + dx, y + dy

def turn_right(direction):
    directions = ['^', '>', 'v', '<']
    idx = directions.index(direction)
    return directions[(idx + 1) % 4]

def simulate_path(start_pos, start_dir, obstacles, max_steps=10000):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    pos = start_pos
    dir_char = start_dir
    visited = set()
    steps = 0

    while steps < max_steps:
        if (pos, dir_char) in visited:
            return True  # Loop detected
        visited.add((pos, dir_char))
        next_pos = next_position(pos, directions[dir_char])

        if next_pos in obstacles:
            # Turn right
            dir_char = turn_right(dir_char)
        else:
            # Move forward
            pos = next_pos

        steps += 1

    return False

def find_loop_positions(grid):
    guard_pos, guard_dir, obstacles = parse_input(grid)
    possible_positions = set()

    # Precompute all empty positions
    empty_positions = [(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '.' and (x, y) != guard_pos]

    for x, y in empty_positions:
        # Try placing an obstruction at (x, y)
        new_obstacles = obstacles | {(x, y)}
        if simulate_path(guard_pos, guard_dir, new_obstacles):
            possible_positions.add((x, y))

    return len(possible_positions)

# Read input from file
with open('input.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

result = find_loop_positions(grid)
print("Number of possible positions to create a loop:", result)
