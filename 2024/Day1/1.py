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
  A = sorted(A)
  B = sorted(B)
  for a, b in zip(A, B):
    result += abs(int(a) - int(b))
  print(result)
