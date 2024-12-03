import Foundation

// Check if all levels are increasing or decreasing
func allIncreasingOrDecreasing(_ arr: [Int]) -> Bool {
    let increasing = zip(arr, arr.dropFirst()).allSatisfy { $0 <= $1 }
    let decreasing = zip(arr, arr.dropFirst()).allSatisfy { $0 >= $1 }
    return increasing || decreasing
}

// Check if all differences are between 1 and 3 inclusive
func isDifferAtLeast1AndAtMost3(_ arr: [Int]) -> Bool {
    return zip(arr, arr.dropFirst()).allSatisfy { abs($0 - $1) >= 1 && abs($0 - $1) <= 3 }
}

// Check if the report is safe without any modifications
func isSafe(_ arr: [Int]) -> Bool {
    return allIncreasingOrDecreasing(arr) && isDifferAtLeast1AndAtMost3(arr)
}

// Check if the report can be made safe by removing a single level
func canBeSafeByRemovingOne(_ arr: [Int]) -> Bool {
    for i in 0..<arr.count {
        var modifiedArr = arr
        modifiedArr.remove(at: i)
        if isSafe(modifiedArr) {
            return true
        }
    }
    return false
}

// Reading the input file
let filePath = "input.txt"
var safeReportsCount = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n")

    for line in lines {
        let levels = line.split(separator: " ").compactMap { Int($0) }
        if isSafe(levels) || canBeSafeByRemovingOne(levels) {
            safeReportsCount += 1
        }
    }

    print("Safe Reports Count: \(safeReportsCount)")

} catch {
    print("Error reading file: \(error)")
}
