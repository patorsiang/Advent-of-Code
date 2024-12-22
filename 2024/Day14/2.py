import re

W = 101
H = 103

robots = []

with open('input.txt', 'r') as f:
    for line in f:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append(((px, py), (vx, vy)))

seconds = 0
while True:
    grid = [[0 for _ in range(W)] for _ in range(H)]
    seconds += 1

    bad = False
    for robot in robots:
        pr1,pr2 = robot
        px,py = pr1
        vx,vy = pr2
        nx,ny = px + seconds*vx, py + seconds*vy
        nx = nx % W
        ny = ny % H
        grid[ny][nx] += 1
        if grid[ny][nx] > 1:
            bad = True

    if not bad:
        for row in grid:
            print("".join(map(str,row)))
        print(seconds)
        break
