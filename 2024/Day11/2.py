import re
import sys

pat_grammar = "[\\d]+"
memo = {}

def count_stones(face, depth, max_depth):
    if depth == max_depth:
        return 1

    key = f"{face}_{depth}"
    if key in memo:
        return memo[key]

    if face == 0:
        stones = count_stones(1, depth + 1, max_depth)
        memo[key] = stones
        return stones

    str_face = str(face)
    if len(str_face) % 2 == 0:
        mid = len(str_face) // 2
        left = int(str_face[:mid])
        right = int(str_face[mid:])
        stones = count_stones(left, depth + 1, max_depth) + count_stones(right, depth + 1, max_depth)
        memo[key] = stones
        return stones

    stones = count_stones(face * 2024, depth + 1, max_depth)
    memo[key] = stones
    return stones

def handle_error(e):
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

with open('input.txt', 'r') as file:
  line = file.readline().strip()
  tokens = re.findall(pat_grammar, line)
  count = 0
  for token in tokens:
    face = int(token)
    count += count_stones(face, 0, 75)
  print(count)
