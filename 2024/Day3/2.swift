import Foundation

// Define the regex pattern to match `do()`, `don't()` or `mul(a, b)`
let pattern = #"(?:(do\(\)|don't\(\))|mul\((\d+),(\d+)\))"#

// Initialize result and state
let filePath = "input.txt"
var result = 0
var enabled = true

// Read the file
do{
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n")

    // Regex initialization
    let regex = try! NSRegularExpression(pattern: pattern, options: [])

    for line in lines {
        // Find matches for `do()`, `don't()` or `mul(a, b)` in the line
        let matches = regex.matches(in: String(line), options: [], range: NSRange(location: 0, length: line.utf16.count))

        for match in matches {
            // Extract instruction and numbers
            let instrRange = match.range(at: 1)
            let aRange = match.range(at: 2)
            let bRange = match.range(at: 3)

            if let instrRange = Range(instrRange, in: line) {
                let instruction = String(line[instrRange])
                if instruction == "don't()" {
                    enabled = false
                } else if instruction == "do()" {
                    enabled = true
                }
            } else if let aRange = Range(aRange, in: line),
                      let bRange = Range(bRange, in: line),
                      enabled {
                // Process `mul(a, b)` if enabled
                let a = Int(line[aRange]) ?? 0
                let b = Int(line[bRange]) ?? 0
                result += a * b
            }
        }
    }
}

// Print the result
print(result)
