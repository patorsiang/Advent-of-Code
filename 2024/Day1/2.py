from collections import Counter
# Reading the entire file
with open("input.txt", "r") as file:
  result = 0
  A = list()
  B = list()
  content = file.readlines()
  for line in content:
    a, b = tuple(filter(lambda x: x, line.strip().split(" ")))
    A.append(a)
    B.append(b)
  count = Counter(B)
  for a in A:
    result += count[a] * int(a)

  print(result)
