import Foundation

func allIncreasingOrDecreasing(_ arr: [Int]) -> Bool {
    // Check if the array is all increasing or all decreasing
    let increasing = zip(arr, arr.dropFirst()).allSatisfy { $0 <= $1 }
    let decreasing = zip(arr, arr.dropFirst()).allSatisfy { $0 >= $1 }
    return increasing || decreasing
}

func isDifferAtLeast1AndAtMost3(_ arr: [Int]) -> Bool {
    // Check if all differences are between 1 and 3 inclusive
    guard let minElement = arr.min(), let maxElement = arr.max() else { return false }
    return minElement >= 1 && maxElement <= 3
}

// Read the input file
let filePath = "input.txt"
var count = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n")

    for line in lines {
        let arr = line.split(separator: " ").compactMap { Int($0) }
        var safeList = [Int]()

        for i in 1..<arr.count {
            safeList.append(abs(arr[i] - arr[i - 1]))
        }

        let cond1 = allIncreasingOrDecreasing(arr)
        let cond2 = isDifferAtLeast1AndAtMost3(safeList)

        if cond1 && cond2 {
            count += 1
        }
    }

    print(count)

} catch {
    print("Error reading file: \(error)")
}
