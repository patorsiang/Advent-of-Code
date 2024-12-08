from itertools import combinations

def parse_map(input_map):
    antennas = []  # List to hold antenna locations and frequencies
    rows = input_map.strip().split("\n")
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))  # Store (x, y, frequency)
    return antennas, len(rows), len(rows[0])

def count_unique_antinodes_complete(input_map):
    antennas, height, width = parse_map(input_map)
    unique_positions = set()

    # Step 1: Include all antenna positions
    for x, y, freq in antennas:
        unique_positions.add((x, y))

    # Step 2: Group by frequency for collinear checks
    frequency_map = {}
    for x, y, freq in antennas:
        if freq not in frequency_map:
            frequency_map[freq] = []
        frequency_map[freq].append((x, y))

    # Step 3: Check all possible pairs of antennas for each frequency
    for freq, positions in frequency_map.items():
        if len(positions) > 1:
            for antenna1, antenna2 in combinations(positions, 2):
                x1, y1 = antenna1
                x2, y2 = antenna2

                dx, dy = x2 - x1, y2 - y1
                gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(__import__('math').gcd(dx, dy))
                step_x, step_y = dx // gcd, dy // gcd

                # Add all points along the line in both directions
                k = 0
                while True:
                    nx, ny = x1 + k * step_x, y1 + k * step_y
                    if 0 <= nx < width and 0 <= ny < height:
                        unique_positions.add((nx, ny))
                    else:
                        break
                    k += 1

                k = -1
                while True:
                    nx, ny = x1 + k * step_x, y1 + k * step_y
                    if 0 <= nx < width and 0 <= ny < height:
                        unique_positions.add((nx, ny))
                    else:
                        break
                    k -= 1

    return len(unique_positions)

with open('input.txt', 'r') as f:
    input_map = f.read()

# Calculate and print the result using the updated resonant harmonics logic
result = count_unique_antinodes_complete(input_map)
print("Number of unique antinode locations:", result)
