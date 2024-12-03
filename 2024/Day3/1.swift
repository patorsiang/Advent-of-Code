import Foundation

// Define the pattern to match `mul(a, b)`
let pattern = #"mul\((\d+),(\d+)\)"#

// Initialize result
let filePath = "input.txt"
var result = 0

// Read the file
do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n")

    // Regex initialization
    let regex = try! NSRegularExpression(pattern: pattern, options: [])
    for line in lines {
        // Find matches for `mul(a, b)` in the line
        let matches = regex.matches(in: String(line), options: [], range: NSRange(location: 0, length: line.utf16.count))

        for match in matches {
            if let aRange = Range(match.range(at: 1), in: line),
            let bRange = Range(match.range(at: 2), in: line) {
                let a = Int(line[aRange]) ?? 0
                let b = Int(line[bRange]) ?? 0
                result += a * b
            }
        }
    }
    print(result)
} catch {
    print("Error reading file: \(error)")
}
