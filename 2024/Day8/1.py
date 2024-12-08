def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = file.read().strip().split("\n")

    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():  # Identifying antennas
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas, len(grid[0]), len(grid)


def calculate_antinodes(antennas, width, height):
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)

        # Iterate over all pairs of antennas with the same frequency
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Midpoint and distances
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                dist_x, dist_y = abs(x1 - x2), abs(y1 - y2)

                # Check if midpoint is valid
                if mid_x.is_integer() and mid_y.is_integer():
                    mid_x, mid_y = int(mid_x), int(mid_y)

                    # Antinodes are valid only if the midpoint is within bounds
                    if 0 <= mid_x < width and 0 <= mid_y < height:
                        antinodes.add((mid_x, mid_y))

                # Generate extrapolated antinodes (twice as far)
                dx, dy = x2 - x1, y2 - y1
                ext1_x, ext1_y = x1 - dx, y1 - dy
                ext2_x, ext2_y = x2 + dx, y2 + dy

                # Check bounds for extrapolated positions
                if 0 <= ext1_x < width and 0 <= ext1_y < height:
                    antinodes.add((ext1_x, ext1_y))
                if 0 <= ext2_x < width and 0 <= ext2_y < height:
                    antinodes.add((ext2_x, ext2_y))

    return antinodes


def count_unique_antinodes(file_path):
    antennas, width, height = parse_input(file_path)
    antinodes = calculate_antinodes(antennas, width, height)
    return len(antinodes)

# Example usage
file_path = "input.txt"  # Replace with your file path
result = count_unique_antinodes(file_path)
print("Number of unique antinode locations:", result)
