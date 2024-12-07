with open("input.txt", "r") as file:
  lines = file.readlines()
  equations = []

  for line in lines:
    parts = line.strip().split(": ")
    test_value = int(parts[0])
    numbers = list(map(lambda x: int(x),parts[1].split(" ")))
    equations.append((test_value, numbers))

def evaluateLeftToRight(numbers, options):
  result = numbers[0]

  for (i, op) in enumerate(options):
    if op == "+":
      result += numbers[i+1]
    elif op == "*":
      result *= numbers[i+1]
    elif op == "|":
      result = int(f"{result}{numbers[i+1]}")

  return result

def genOperationCombinations(l):
  opt = ["+", "*", "|"]
  combinations = []

  def backtrack (current):
    if len(current) == l - 1:
      combinations.append(current)
      return

    for op in opt:
      backtrack(current + [op])

  backtrack([])
  return combinations


totalCalibrationResult = 0

for (testValue, numbers) in equations:
  valid = False
  operations = genOperationCombinations(len(numbers))
  for ops in operations:
    if evaluateLeftToRight(numbers, ops) == testValue:
      valid = True
      break

  if valid:
    totalCalibrationResult += testValue

print(totalCalibrationResult)
