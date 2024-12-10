import Foundation

// Read input from a file
let inputMap = try String(contentsOfFile: "input.txt", encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)

var num = 0
var s: [String] = []

// Process the input map
for (i, char) in inputMap.enumerated() {
    if let n = Int(String(char)) {
        for _ in 0..<n {
            if i % 2 == 0 {
                s.append(String(num))
            } else {
                s.append(".")
            }
        }
        if i % 2 == 0 {
            num += 1
        }
    }
}

var i = 0
var j = s.count - 1

// Perform the file compaction
while i < j && j >= 0 && i < s.count {
    if s[i] == "." {
        s[i] = s[j]
        s[j] = "."
        j -= 1
    } else {
        i += 1
    }
}

var res = 0

// Calculate the checksum
for (i, n) in s.enumerated() {
    if n == "." {
        break
    }
    if let value = Int(n) {
        res += i * value
    }
}

print(res)
