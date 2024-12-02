def all_increasing_or_decreasing(arr):
  """all increasing or decreasing return true"""
  return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or all(arr[i] >= arr[i+1] for i in range(len(arr)-1))

def is_differ_at_least_1_and_at_most_3(arr):
  """is differ at least 1 and at most 3 return true"""
  return min(arr) >= 1 and max(arr) <= 3

with open("input.txt", "r") as file:
  content = file.readlines()
  count = 0
  for line in content:
    arr = list(map(lambda x: int(x), line.strip().split(" ")))
    safe_list = list()
    for i in range(1, len(arr)):
      safe_list.append(abs(arr[i] - arr[i-1]))
    cond1 = all_increasing_or_decreasing(arr)
    cond2 = is_differ_at_least_1_and_at_most_3(safe_list)
    if cond1 and cond2:
      count += 1

  print(count)
