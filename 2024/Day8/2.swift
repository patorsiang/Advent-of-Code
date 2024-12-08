import Foundation

func parseMap(_ inputMap: String) -> ([(Int, Int, Character)], Int, Int) {
    var antennas: [(Int, Int, Character)] = []
    let rows = inputMap.split(separator: "\n")
    for (y, row) in rows.enumerated() {
        for (x, char) in row.enumerated() {
            if char != "." {
                antennas.append((x, y, char))
            }
        }
    }
    return (antennas, rows.count, rows.first?.count ?? 0)
}

func gcd(_ a: Int, _ b: Int) -> Int {
    var a = a
    var b = b
    while b != 0 {
        let temp = b
        b = a % b
        a = temp
    }
    return abs(a)
}

func countUniqueAntinodesComplete(_ inputMap: String) -> Int {
    let (antennas, height, width) = parseMap(inputMap)
    var uniquePositions = Set<NSString>()

    // Step 1: Include all antenna positions
    for (x, y, _) in antennas {
        uniquePositions.insert(NSString(string: "\(x),\(y)"))
    }

    // Step 2: Group by frequency for collinear checks
    var frequencyMap: [Character: [(Int, Int)]] = [:]
    for (x, y, freq) in antennas {
        frequencyMap[freq, default: []].append((x, y))
    }

    // Step 3: Check all possible pairs of antennas for each frequency
    for (_, positions) in frequencyMap {
        if positions.count > 1 {
            for i in 0..<(positions.count - 1) {
                for j in (i + 1)..<positions.count {
                    let (x1, y1) = positions[i]
                    let (x2, y2) = positions[j]

                    let dx = x2 - x1
                    let dy = y2 - y1
                    let stepGCD = gcd(dx, dy)
                    let stepX = dx / stepGCD
                    let stepY = dy / stepGCD

                    // Add all points along the line in both directions
                    var k = 0
                    while true {
                        let nx = x1 + k * stepX
                        let ny = y1 + k * stepY
                        if nx >= 0 && nx < width && ny >= 0 && ny < height {
                            uniquePositions.insert(NSString(string: "\(nx),\(ny)"))
                        } else {
                            break
                        }
                        k += 1
                    }

                    k = -1
                    while true {
                        let nx = x1 + k * stepX
                        let ny = y1 + k * stepY
                        if nx >= 0 && nx < width && ny >= 0 && ny < height {
                            uniquePositions.insert(NSString(string: "\(nx),\(ny)"))
                        } else {
                            break
                        }
                        k -= 1
                    }
                }
            }
        }
    }

    return uniquePositions.count
}

// Read the input map from a file
if let inputMap = try? String(contentsOfFile: "input.txt", encoding: .utf8) {
    let result = countUniqueAntinodesComplete(inputMap)
    print("Number of unique antinode locations:", result)
}
