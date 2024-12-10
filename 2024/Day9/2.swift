import Foundation

// Read input from a file with specified encoding
let inputMap = try String(contentsOfFile: "input.txt", encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)

var num = 0
var M = 0
var s: [[String]] = []

// Process the input map
for (i, char) in inputMap.enumerated() {
    if let n = Int(String(char)) {
        var sub: [String] = []
        for _ in 0..<n {
            if i % 2 == 0 {
                sub.append(String(num))
                M = num
            } else {
                sub.append(".")
            }
        }
        if !sub.isEmpty {
            s.append(sub)
        }
        if i % 2 == 0 {
            num += 1
        }
    }
}

// Function to merge dots
func mergeDot(_ s: inout [[String]]) {
    var i = 0
    while i < s.count {
        let el = s[i]
        if el.contains(".") {
            if !el.allSatisfy({ $0 == "." }) {
                if let j = el.firstIndex(of: ".") {
                    let first = Array(el[..<j])
                    let second = Array(el[j...])
                    s.remove(at: i)
                    if i < s.count, s[i][0] == "." {
                        s[i].insert(contentsOf: second, at: 0)
                    } else {
                        s.insert(second, at: i)
                    }
                    s.insert(first, at: i)
                }
            } else if i + 1 < s.count,
                      el.allSatisfy({ $0 == "." }),
                      s[i + 1].allSatisfy({ $0 == "." }) {
                s[i].append(contentsOf: s[i + 1])
                s.remove(at: i + 1)
                i -= 1
            }
        }
        i += 1
    }
    s = s.filter { !$0.isEmpty }
}

// Function to find j
func findJ(_ s: [[String]]) -> Int {
    for (i, el) in s.enumerated() {
        if el.contains(String(M)) {
            M -= 1
            return i
        }
    }
    return -1
}

var j = findJ(s)

// Perform the main loop
while j > -1 {
    var i = 0
    if !s[j].contains(".") {
        while i < j {
            if s[i][0] == "." && s[i].count >= s[j].count {
                for tmpI in 0..<s[j].count {
                    s[i][tmpI] = s[j][tmpI]
                    s[j][tmpI] = "."
                }
                mergeDot(&s)
                break
            }
            i += 1
        }
    }
    j = findJ(s)
    print(j)
}

let flattenedS = s.flatMap { $0 }
var res = 0

// Calculate the checksum
for (i, n) in flattenedS.enumerated() {
    if n != "." {
        if let value = Int(n) {
            res += i * value
        }
    }
}

print(res)
