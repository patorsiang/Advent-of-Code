def all_increasing_or_decreasing(arr):
    """Check if all levels are increasing or decreasing."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

def is_differ_at_least_1_and_at_most_3(arr):
    """Check if all differences are between 1 and 3 inclusive."""
    return all(1 <= abs(arr[i] - arr[i - 1]) <= 3 for i in range(1, len(arr)))

def is_safe(arr):
    """Check if the report is safe without any modifications."""
    return all_increasing_or_decreasing(arr) and is_differ_at_least_1_and_at_most_3(arr)

def can_be_safe_by_removing_one(arr):
    """Check if the report can be made safe by removing a single level."""
    for i in range(len(arr)):
        modified_arr = arr[:i] + arr[i + 1:]  # Remove the i-th level
        if is_safe(modified_arr):
            return True
    return False

# Reading the input data
with open("input.txt", "r") as file:
    content = file.readlines()

safe_reports_count = 0

for line in content:
    levels = list(map(int, line.strip().split()))
    if is_safe(levels) or can_be_safe_by_removing_one(levels):
        safe_reports_count += 1

print(safe_reports_count)
