import Foundation

func countXMAS(grid: [[Character]], word: String = "XMAS") -> Int {
    let rows = grid.count
    let cols = grid[0].count
    let wordLength = word.count
    let directions = [
        (0, 1),   // Right
        (1, 0),   // Down
        (1, 1),   // Diagonal down-right
        (1, -1),  // Diagonal down-left
        (0, -1),  // Left
        (-1, 0),  // Up
        (-1, -1), // Diagonal up-left
        (-1, 1)   // Diagonal up-right
    ]

    func inBounds(row: Int, col: Int) -> Bool {
        return row >= 0 && row < rows && col >= 0 && col < cols
    }

    func match(row: Int, col: Int, dr: Int, dc: Int) -> Bool {
        for i in 0..<wordLength {
            let nr = row + i * dr
            let nc = col + i * dc
            if !inBounds(row: nr, col: nc) || grid[nr][nc] != word[word.index(word.startIndex, offsetBy: i)] {
                return false
            }
        }
        return true
    }

    var count = 0

    for row in 0..<rows {
        for col in 0..<cols {
            for (dr, dc) in directions {
                if match(row: row, col: col, dr: dr, dc: dc) {
                    count += 1
                }
            }
        }
    }

    return count
}

// Read input from file
let fileURL = URL(fileURLWithPath: "input.txt")
if let content = try? String(contentsOf: fileURL, encoding: .utf8) {
    let grid = content.split(separator: "\n").map { Array($0) }
    let result = countXMAS(grid: grid)
    print("Total occurrences of 'XMAS': \(result)")
} else {
    print("Error reading the file.")
}
