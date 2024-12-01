import Foundation

// File path (replace with the correct path to your file)
let filePath = "input.txt"

do {
    // Read the entire file
    let content = try String(contentsOfFile: filePath, encoding: .utf8)

    var A = [Int]()
    var B = [Int]()
    var result = 0

    // Split the content into lines
    let lines = content.split(separator: "\n")

    // Process each line
    for line in lines {
        let parts = line.split(separator: " ").filter { !$0.isEmpty }
        if let a = Int(parts[0]), let b = Int(parts[1]) {
            A.append(a)
            B.append(b)
        }
    }

    // Create a frequency dictionary for B (similar to Counter in Python)
    var count: [Int: Int] = [:]
    for b in B {
        count[b, default: 0] += 1
    }

    // Calculate the result
    for a in A {
        if let freq = count[a] {
            result += freq * a
        }
    }

    // Print the result
    print(result)

} catch {
    print("Error reading file: \(error)")
}
