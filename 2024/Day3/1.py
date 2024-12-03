import re

pattern = r"mul\((\d+),(\d+)\)"

res = 0

with open('input.txt', 'r') as file:
  text = file.readlines()
  for line in text:
    matches = re.findall(pattern, line.strip())
    for a, b in matches:
      res += int(a) * int(b)
print(res)
