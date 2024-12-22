import re
import numpy as np

# Space dimensions
WIDTH = 101
HEIGHT = 103

# Parse the input
robots = []
with open('input.txt', 'r') as f:
    for line in f:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append(((px, py), (vx, vy)))

# Simulate motion for 100 seconds
final_positions = []
for (px, py), (vx, vy) in robots:
    x_final = (px + 100 * vx) % WIDTH
    y_final = (py + 100 * vy) % HEIGHT
    final_positions.append((x_final, y_final))

# Count robots in each quadrant
count_top_left = 0
count_top_right = 0
count_bottom_left = 0
count_bottom_right = 0

for x, y in final_positions:
    if x == WIDTH // 2 or y == HEIGHT // 2:
        continue  # Skip robots on dividing lines
    if x < WIDTH // 2 and y < HEIGHT // 2:
        count_top_left += 1
    elif x >= WIDTH // 2 and y < HEIGHT // 2:
        count_top_right += 1
    elif x < WIDTH // 2 and y >= HEIGHT // 2:
        count_bottom_left += 1
    elif x >= WIDTH // 2 and y >= HEIGHT // 2:
        count_bottom_right += 1

# Calculate the safety factor
safety_factor = (count_top_left) * (count_top_right) * (count_bottom_left) * (count_bottom_right)

print(f"Top-left: {count_top_left}")
print(f"Top-right: {count_top_right}")
print(f"Bottom-left: {count_bottom_left}")
print(f"Bottom-right: {count_bottom_right}")
print(f"Safety Factor: {safety_factor}")
