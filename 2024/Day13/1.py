import re

def parse_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
          txt = line.strip()
          if txt.startswith("Button"):
              pattern = r"X\+(\d+), Y\+(\d+)"
              match = re.search(pattern, line)
              if 'A' in txt:
                a_x, a_y = int(match.group(1)), int(match.group(2))
              elif 'B' in txt:
                b_x, b_y = int(match.group(1)), int(match.group(2))
          elif txt.startswith("Prize"):
              pattern = r"X=(\d+), Y=(\d+)"
              match = re.search(pattern, line)
              p_x, p_y = int(match.group(1)), int(match.group(2))
              machines.append(((a_x, a_y), (b_x, b_y), (p_x, p_y)))

    return machines

def solve_machine(a, b, prize):
    a_x, a_y = a
    b_x, b_y = b
    p_x, p_y = prize
    min_cost = float('inf')
    found = False

    for a_count in range(101):  # Limit button presses to 100
        for b_count in range(101):
            if a_count * a_x + b_count * b_x == p_x and a_count * a_y + b_count * b_y == p_y:
                cost = 3 * a_count + b_count
                if cost < min_cost:
                    min_cost = cost
                    found = True
    return min_cost if found else None

def main(file_path):
    machines = parse_input(file_path)
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        a, b, prize = machine
        cost = solve_machine(a, b, prize)
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    print(f"Prizes won: {prizes_won}")
    print(f"Total cost: {total_cost}")

# Replace 'input.txt' with the path to your file
main("input.txt")
