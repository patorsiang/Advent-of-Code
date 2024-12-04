import Foundation

func countXMASXPattern(grid: [[Character]]) -> Int {
    let rows = grid.count
    let cols = grid[0].count
    var count = 0

    // Check if a cell (r, c) is part of an "X-MAS" pattern
    func isXMAS(r: Int, c: Int) -> Bool {
        // Check bounds for the cross structure
        guard r > 0 && r < rows - 1 && c > 0 && c < cols - 1 else {
            return false
        }
        // Possible "MAS" patterns
        let masVariants = ["MAS", "SAM"]

        // Check the X-MAS pattern
        let topLeft = String([grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]])
        let topRight = String([grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]])

        return masVariants.contains(topLeft) && masVariants.contains(topRight)
    }

    // Iterate through the grid
    for r in 1..<rows - 1 {
        for c in 1..<cols - 1 {
            if isXMAS(r: r, c: c) {
                count += 1
            }
        }
    }

    return count
}

// Read the grid from a file
let fileURL = URL(fileURLWithPath: "input.txt")
if let content = try? String(contentsOf: fileURL, encoding: .utf8) {
    let grid = content.split(separator: "\n").map { Array($0) }
    let result = countXMASXPattern(grid: grid)
    print("Total occurrences of 'X-MAS': \(result)")
} else {
    print("Error reading the file.")
}
