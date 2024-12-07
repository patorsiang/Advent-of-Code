import Foundation

func evaluateLeftToRight(numbers: [Int], operators: [Character]) -> Int {
    var result = numbers[0]
    for (index, op) in operators.enumerated() {
        if op == "+" {
            result += numbers[index + 1]
        } else if op == "*" {
            result *= numbers[index + 1]
        }
    }
    return result
}

func generateOperatorCombinations(count: Int) -> [[Character]] {
    let operators: [Character] = ["+", "*"]
    var combinations: [[Character]] = []

    func backtrack(current: [Character]) {
        if current.count == count {
            combinations.append(current)
            return
        }
        for op in operators {
            backtrack(current: current + [op])
        }
    }

    backtrack(current: [])
    return combinations
}

func parseInput(input: String) -> [(Int, [Int])] {
    let lines = input.split(separator: "\n")
    var equations: [(Int, [Int])] = []

    for line in lines {
        let parts = line.split(separator: ":")
        let testValue = Int(parts[0].trimmingCharacters(in: .whitespaces))!
        let numbers = parts[1].split(separator: " ").compactMap { Int($0) }
        equations.append((testValue, numbers))
    }

    return equations
}

func readInputFromFile(filePath: String) -> String? {
    do {
        return try String(contentsOfFile: filePath, encoding: .utf8)
    } catch {
        print("Error reading file: \(error)")
        return nil
    }
}

func calculateCalibrationResult(input: String) -> Int {
    let equations = parseInput(input: input)
    var totalCalibrationResult = 0

    for (testValue, numbers) in equations {
        let operatorCombinations = generateOperatorCombinations(count: numbers.count - 1)
        var valid = false

        for ops in operatorCombinations {
            if evaluateLeftToRight(numbers: numbers, operators: ops) == testValue {
                valid = true
                break
            }
        }

        if valid {
            totalCalibrationResult += testValue
        }
    }

    return totalCalibrationResult
}

// Example usage with file input
if let input = readInputFromFile(filePath: "input.txt") {
    let result = calculateCalibrationResult(input: input)
    print("The total calibration result is \(result).")
} else {
    print("Failed to read input from file.")
}
