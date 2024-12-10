import Foundation

func parseMap(inputMap: String) -> [[Int]] {
    return inputMap.split(separator: "\n").map { line in
        line.compactMap { $0.wholeNumberValue }
    }
}

func findTrailheads(topographicMap: [[Int]]) -> [[Int]] {
    var trailheads: [[Int]] = []
    for (r, row) in topographicMap.enumerated() {
        for (c, value) in row.enumerated() {
            if value == 0 {
                trailheads.append([r, c])
            }
        }
    }
    return trailheads
}

func isValidMove(currentHeight: Int, nextHeight: Int) -> Bool {
    return nextHeight == currentHeight + 1
}

func bfsForScore(topographicMap: [[Int]], start: [Int]) -> Int {
    let rows = topographicMap.count
    let cols = topographicMap[0].count
    var queue: [[Int]] = [start]
    var visited: Set<[Int]> = []
    var reachableNines: Set<[Int]> = []

    while !queue.isEmpty {
        let position = queue.removeFirst()
        let r = position[0], c = position[1]
        if visited.contains(position) {
            continue
        }
        visited.insert(position)

        let currentHeight = topographicMap[r][c]
        if currentHeight == 9 {
            reachableNines.insert(position)
        }

        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
            let nr = r + dr
            let nc = c + dc
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                let nextHeight = topographicMap[nr][nc]
                if isValidMove(currentHeight: currentHeight, nextHeight: nextHeight) {
                    queue.append([nr, nc])
                }
            }
        }
    }

    return reachableNines.count
}

func bfsForRating(topographicMap: [[Int]], start: [Int]) -> Int {
    let rows = topographicMap.count
    let cols = topographicMap[0].count
    var queue: [([Int], Set<[Int]>)] = [(start, Set([start]))]
    var distinctTrails: Set<Set<[Int]>> = []

    while !queue.isEmpty {
        let (position, path) = queue.removeFirst()
        let r = position[0], c = position[1]
        let currentHeight = topographicMap[r][c]

        if currentHeight == 9 {
            distinctTrails.insert(path)
            continue
        }

        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
            let nr = r + dr
            let nc = c + dc
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                let nextHeight = topographicMap[nr][nc]
                if isValidMove(currentHeight: currentHeight, nextHeight: nextHeight) && !path.contains([nr, nc]) {
                    var newPath = path
                    newPath.insert([nr, nc])
                    queue.append(([nr, nc], newPath))
                }
            }
        }
    }

    return distinctTrails.count
}

func calculateTotalScore(topographicMap: [[Int]]) -> Int {
    let trailheads = findTrailheads(topographicMap: topographicMap)
    return trailheads.reduce(0) { total, trailhead in
        total + bfsForScore(topographicMap: topographicMap, start: trailhead)
    }
}

func calculateTotalRating(topographicMap: [[Int]]) -> Int {
    let trailheads = findTrailheads(topographicMap: topographicMap)
    return trailheads.reduce(0) { total, trailhead in
        total + bfsForRating(topographicMap: topographicMap, start: trailhead)
    }
}

// Read input from file
let fileManager = FileManager.default
let inputPath = fileManager.currentDirectoryPath.appending("/input.txt")
if let inputMap = try? String(contentsOfFile: inputPath, encoding: .utf8) {
    let topographicMap = parseMap(inputMap: inputMap)
    let scoreResult = calculateTotalScore(topographicMap: topographicMap)
    let ratingResult = calculateTotalRating(topographicMap: topographicMap)
    print("Total score of all trailheads:", scoreResult)
    print("Total rating of all trailheads:", ratingResult)
} else {
    print("Failed to read input file.")
}
