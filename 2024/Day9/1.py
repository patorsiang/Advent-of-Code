with open('input.txt', 'r') as f:
  input_map = f.read().strip()

num = 0
s = []
for i, n in enumerate(input_map):
  n = int(n)
  for _ in range(n):
    if i % 2 == 0:
      s.append(num)
    else:
      s.append('.')
  if i % 2 == 0:
    num += 1

i = 0
j = len(s) - 1

while i < j and j > -1 and i < len(s):
  if s[i] == '.':
    s[i] = s[j]
    s[j] = '.'
    j -= 1
  else:
    i += 1

res = 0
for i, n in enumerate(s):
  if n == '.':
    break
  res += i * int(n)

print(res)
