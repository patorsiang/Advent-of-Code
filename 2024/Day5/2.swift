import Foundation

let filePath = "input.txt"

struct Rule: Hashable {
    let x: Int
    let y: Int
}

func parseRules(_ ruleLines: [String]) -> Set<Rule> {
    var rules = Set<Rule>()
    for rule in ruleLines {
        let parts = rule.split(separator: "|").compactMap { Int($0) }
        if parts.count == 2 {
            rules.insert(Rule(x: parts[0], y: parts[1]))
        }
    }
    return rules
}

func isValidUpdate(_ update: [Int], rules: Set<Rule>) -> Bool {
    for i in 0..<update.count {
        for j in (i + 1)..<update.count {
            let x = update[i], y = update[j]
            if rules.contains(Rule(x: y, y: x)) { // If there's a rule Y|X, this order is invalid
                return false
            }
        }
    }
    return true
}

func findMiddlePage(_ update: [Int]) -> Int {
    return update[update.count / 2]
}

func reorderUpdate(_ update: [Int], rules: Set<Rule>) -> [Int] {
    var graph = [Int: [Int]]()
    var inDegree = [Int: Int]()
    let pagesInUpdate = Set(update)

    // Build the graph and compute in-degrees
    for rule in rules {
        if pagesInUpdate.contains(rule.x) && pagesInUpdate.contains(rule.y) {
            graph[rule.x, default: []].append(rule.y)
            inDegree[rule.y, default: 0] += 1
            if inDegree[rule.x] == nil {
                inDegree[rule.x] = 0
            }
        }
    }

    // Perform topological sort
    var queue = [Int]()
    for page in update {
        if inDegree[page, default: 0] == 0 {
            queue.append(page)
        }
    }

    var sortedOrder = [Int]()
    while !queue.isEmpty {
        let node = queue.removeFirst()
        sortedOrder.append(node)
        for neighbor in graph[node, default: []] {
            inDegree[neighbor, default: 0] -= 1
            if inDegree[neighbor, default: 0] == 0 {
                queue.append(neighbor)
            }
        }
    }

    return sortedOrder
}

do {
  let content = try String(contentsOfFile: filePath, encoding: .utf8)

  let lines = content.split(separator: "\n").map { String($0) }

  var rulesSection = [String]()
  var updatesSection = [String]()
  var parsingRules = true

  for line in lines {
    if line.contains(",") {
      parsingRules = false
    }
    if parsingRules {
      rulesSection.append(line)
    } else {
      updatesSection.append(line)
    }
  }

  // Parse rules
  let rules = parseRules(rulesSection)

  var invalidUpdates = [[Int]]()
  for updateLine in updatesSection {
        let update = updateLine.split(separator: ",").compactMap { Int($0) }
        if !isValidUpdate(update, rules: rules) {
            invalidUpdates.append(update)
        }
  }

  var totalMiddleSum = 0
    for update in invalidUpdates {
        let correctedUpdate = reorderUpdate(update, rules: rules)
        totalMiddleSum += findMiddlePage(correctedUpdate)
    }

  print("Total Middle Sum: \(totalMiddleSum)")

} catch {
  print("Error: \(error)")
}
