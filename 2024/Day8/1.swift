import Foundation

struct Position: Hashable {
    let x: Int
    let y: Int
}

func parseInput(from filePath: String) -> (antennas: [Character: [Position]], width: Int, height: Int)? {
    do {
        let content = try String(contentsOfFile: filePath, encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)
        let grid = content.split(separator: "\n")

        var antennas = [Character: [Position]]()

        for (y, row) in grid.enumerated() {
            for (x, char) in row.enumerated() {
                if char.isLetter || char.isNumber {
                    antennas[char, default: []].append(Position(x: x, y: y))
                }
            }
        }

        let width = grid.first?.count ?? 0
        let height = grid.count

        return (antennas, width, height)
    } catch {
        print("Error reading file: \(error)")
        return nil
    }
}

func calculateAntinodes(antennas: [Character: [Position]], width: Int, height: Int) -> Set<Position> {
    var antinodes = Set<Position>()

    for (_, positions) in antennas {
        let n = positions.count

        for i in 0..<n {
            for j in (i + 1)..<n {
                let p1 = positions[i]
                let p2 = positions[j]

                // Midpoint and distances
                let midX = (p1.x + p2.x) / 2
                let midY = (p1.y + p2.y) / 2

                // Check if midpoint is valid
                if (p1.x + p2.x) % 2 == 0 && (p1.y + p2.y) % 2 == 0 {
                    if midX >= 0 && midX < width && midY >= 0 && midY < height {
                        antinodes.insert(Position(x: midX, y: midY))
                    }
                }

                // Generate extrapolated antinodes (twice as far)
                let dx = p2.x - p1.x
                let dy = p2.y - p1.y
                let ext1 = Position(x: p1.x - dx, y: p1.y - dy)
                let ext2 = Position(x: p2.x + dx, y: p2.y + dy)

                if ext1.x >= 0 && ext1.x < width && ext1.y >= 0 && ext1.y < height {
                    antinodes.insert(ext1)
                }
                if ext2.x >= 0 && ext2.x < width && ext2.y >= 0 && ext2.y < height {
                    antinodes.insert(ext2)
                }
            }
        }
    }

    return antinodes
}

func countUniqueAntinodes(filePath: String) -> Int {
    guard let (antennas, width, height) = parseInput(from: filePath) else {
        return 0
    }
    let antinodes = calculateAntinodes(antennas: antennas, width: width, height: height)
    return antinodes.count
}

// Example usage
let filePath = "input.txt"  // Replace with your file path
let result = countUniqueAntinodes(filePath: filePath)
print("Number of unique antinode locations: \(result)")
