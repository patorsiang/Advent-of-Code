import time
from datetime import datetime

def do_rule(num):
    """Apply transformation rules to a single number."""
    if num == 0:
        return [1]
    num_str = str(num)
    length = len(num_str)
    if length % 2 == 0:
        mid = length // 2
        return [int(num_str[:mid]), int(num_str[mid:])]
    else:
        return [num * 2024]


with open('input.txt', 'r') as f:
  nums = list(map(int, f.read().strip().split()))

def do_nums(nums):
  new_nums = []
  amount = len(nums)

  for i in range(amount//2):
    new_nums.extend(do_rule(nums[i]))
    new_nums.extend(do_rule(nums[amount - i - 1]))

  if amount % 2 == 1:
    new_nums.extend(do_rule(nums[amount//2]))

  return new_nums

blinks = 25

start_time_total = time.time()

for blink in range(1, blinks + 1):
  start_time = time.time()
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  nums = do_nums(nums)
  end_time = time.time()
  # Output the number of stones
  elapsed_time = end_time - start_time
  print(f"[{current_time}] Blink {blink}: {len(nums)} stones (Elapsed time: {elapsed_time:.2f} seconds)")

print(f"Total Execution time: {end_time - start_time_total:.2f} seconds")
