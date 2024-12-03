import re

pattern = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"

res = 0
enable = True

with open('input.txt', 'r') as file:
  text = file.readlines()
  for line in text:
    matches = re.findall(pattern, line.strip())
    for instr, a, b in matches:
      if instr == "don't()":
        enable = False
      elif instr == "do()":
        enable = True
      elif enable:
        res += int(a) * int(b)
print(res)
