import Foundation

func simulateGuardPatrol(grid: [[Character]]) -> Int {
    let rows = grid.count
    let cols = grid[0].count

    // Locate the guard's starting position and direction
    let directions: [Character: (Int, Int)] = [
        "^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)
    ]
    let directionSymbols: [Character] = ["^", ">", "v", "<"]

    var guardPosition: (Int, Int)? = nil
    var directionIndex = 0

    outerLoop: for r in 0..<rows {
        for c in 0..<cols {
            if let _ = directions[grid[r][c]] {
                guardPosition = (r, c)
                directionIndex = directionSymbols.firstIndex(of: grid[r][c])!
                break outerLoop
            }
        }
    }

    guard let startGuardPosition = guardPosition else {
        return 0
    }

    var visitedPositions: Set<[Int]> = [ [startGuardPosition.0, startGuardPosition.1] ]
    var currentGuardPosition = startGuardPosition

    while true {
        let currentDirection = directionSymbols[directionIndex]
        let (dr, dc) = directions[currentDirection]!
        let nextR = currentGuardPosition.0 + dr
        let nextC = currentGuardPosition.1 + dc

        // Check if the guard is about to leave the map
        if !(0 <= nextR && nextR < rows && 0 <= nextC && nextC < cols) {
            break
        }

        // If there's an obstacle, turn right
        if grid[nextR][nextC] == "#" {
            directionIndex = (directionIndex + 1) % 4
        } else {
            // Move forward
            currentGuardPosition = (nextR, nextC)
            visitedPositions.insert([currentGuardPosition.0, currentGuardPosition.1])
        }
    }

    return visitedPositions.count
}

func readGridFromFile(filePath: String) -> [[Character]]? {
    do {
        let content = try String(contentsOfFile: filePath, encoding: .utf8)
        let lines = content.split(separator: "\n").map { Array($0) }
        return lines
    } catch {
        print("Error reading file: \(error)")
        return nil
    }
}

// Example usage with file input
if let grid = readGridFromFile(filePath: "input.txt") {
    let result = simulateGuardPatrol(grid: grid)
    print("The guard visited \(result) distinct positions.")
} else {
    print("Failed to read grid from file.")
}
