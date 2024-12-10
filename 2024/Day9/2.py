with open('input.txt', 'r') as f:
  input_map = f.read().strip()

num = 0
M = 0
s = []
for i, n in enumerate(input_map):
  n = int(n)
  sub = []
  for _ in range(n):
    if i % 2 == 0:
      sub.append(num)
      M = num
    else:
      sub.append('.')
  if len(sub) > 0:
    s.append(sub)
  if i % 2 == 0:
    num += 1

def merge_dot(s):
  i = 0
  while i < len(s):
    el = s[i]
    if '.' in el:
      if not all(list(map(lambda x: x == '.', el))):
        j = el.index('.')
        first = el[:j]
        second = el[j:]
        del s[i]
        if len(s[i]) > 0 and s[i][0] == '.':
          s[i].extend(second)
        else:
          s.insert(i, second)
        s.insert(i, first)
      elif i+1 < len(s) and all(list(map(lambda x: x == '.', el))) and all(list(map(lambda x: x == '.', s[i+1]))):
        s[i].extend(s[i+1])
        del s[i+1]
        i -= 1
    i += 1
  return list(filter(lambda x: len(x) > 0, s))

def find_j(s):
  global M
  for i, el in enumerate(s):
    if M in el:
      M -= 1
      return i
  return -1

j = find_j(s)

# print(M, s)
while j > -1:
  i = 0
  if '.' not in s[j]:
    while i < j:
      if s[i][0] == '.' and len(s[i]) >= len(s[j]):
        for tmp_i, tmp_n in enumerate(s[j]):
          s[i][tmp_i] = tmp_n
          s[j][tmp_i] = '.'
        s = merge_dot(s)
        # print(M, s)
        break
      i += 1
  j = find_j(s)
  print(j, i)

s = sum(s, [])
res = 0
for i, n in enumerate(s):
  if n != '.':
    res += i * int(n)

print(res)
