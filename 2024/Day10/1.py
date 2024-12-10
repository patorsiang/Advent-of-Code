from collections import deque

def parse_map(input_map):
    return [list(map(int, line)) for line in input_map.strip().split("\n")]

def find_trailheads(topographic_map):
    trailheads = []
    for r in range(len(topographic_map)):
        for c in range(len(topographic_map[0])):
            if topographic_map[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(current_height, next_height):
    return next_height == current_height + 1

def bfs(topographic_map, start):
    rows, cols = len(topographic_map), len(topographic_map[0])
    queue = deque([start])
    visited = set()
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        current_height = topographic_map[r][c]
        if current_height == 9:
            reachable_nines.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_height = topographic_map[nr][nc]
                if is_valid_move(current_height, next_height):
                    queue.append((nr, nc))

    return len(reachable_nines)

def calculate_total_score(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_score = 0
    for trailhead in trailheads:
        total_score += bfs(topographic_map, trailhead)
    return total_score

# Read input from file
with open("input.txt", "r") as file:
    input_map = file.read()

topographic_map = parse_map(input_map)
result = calculate_total_score(topographic_map)
print("Total score of all trailheads:", result)
