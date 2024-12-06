import Foundation

struct Position: Hashable {
    let x: Int
    let y: Int
}

struct GuardSimulation {
    var guardPos: Position
    var guardDir: Character
    var obstacles: Set<Position>
    let directions: [Character: (x: Int, y: Int)] = [
        "^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)
    ]

    init(grid: [String]) {
        var guardPosition: Position? = nil
        var guardDirection: Character? = nil
        var obstaclesSet = Set<Position>()

        for (y, line) in grid.enumerated() {
            for (x, char) in line.enumerated() {
                if char == "#" {
                    obstaclesSet.insert(Position(x: x, y: y))
                } else if directions.keys.contains(char) {
                    guardPosition = Position(x: x, y: y)
                    guardDirection = char
                }
            }
        }

        self.guardPos = guardPosition!
        self.guardDir = guardDirection!
        self.obstacles = obstaclesSet
    }

    func nextPosition(_ position: Position, _ direction: (x: Int, y: Int)) -> Position {
        return Position(x: position.x + direction.x, y: position.y + direction.y)
    }

    func turnRight(_ direction: Character) -> Character {
        let directionsOrder: [Character] = ["^", ">", "v", "<"]
        if let idx = directionsOrder.firstIndex(of: direction) {
            return directionsOrder[(idx + 1) % directionsOrder.count]
        }
        return direction
    }

    func simulatePath(startPos: Position, startDir: Character, obstacles: Set<Position>, maxSteps: Int = 10000) -> Bool {
        var pos = startPos
        var dirChar = startDir
        var visited = Set<VisitedState>()
        var steps = 0

        while steps < maxSteps {
            let currentState = VisitedState(position: pos, direction: dirChar)
            if visited.contains(currentState) {
                return true // Loop detected
            }
            visited.insert(currentState)
            let direction = directions[dirChar]!
            let nextPos = nextPosition(pos, direction)

            if obstacles.contains(nextPos) {
                // Turn right
                dirChar = turnRight(dirChar)
            } else {
                // Move forward
                pos = nextPos
            }

            steps += 1
        }

        return false
    }

    func findLoopPositions(grid: [String]) -> Int {
        var possiblePositions = Set<Position>()

        // Precompute all empty positions
        var emptyPositions = [Position]()
        for (y, line) in grid.enumerated() {
            for (x, char) in line.enumerated() {
                if char == "." && Position(x: x, y: y) != guardPos {
                    emptyPositions.append(Position(x: x, y: y))
                }
            }
        }

        let checkPosition: (Position) -> Position? = { position in
            var newObstacles = self.obstacles
            newObstacles.insert(position)
            return self.simulatePath(startPos: self.guardPos, startDir: self.guardDir, obstacles: newObstacles) ? position : nil
        }

        let results = emptyPositions.compactMap { checkPosition($0) }
        possiblePositions = Set(results)

        return possiblePositions.count
    }
}

struct VisitedState: Hashable {
    let position: Position
    let direction: Character
}

let fileURL = URL(fileURLWithPath: "input.txt")
// Read input from file
if let content = try? String(contentsOf: fileURL, encoding: .utf8) {
    let grid = content.split(separator: "\n").map { String($0) }
    let simulation = GuardSimulation(grid: grid)
    let result = simulation.findLoopPositions(grid: grid)
    print("Number of possible positions to create a loop: \(result)")
}
