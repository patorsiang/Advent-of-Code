from collections import defaultdict, deque

def parse_rules(rule_lines):
    rules = {}
    for rule in rule_lines:
        x, y = map(int, rule.split("|"))
        rules[(x, y)] = True  # X must come before Y
    return rules

def is_valid_update(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if (y, x) in rules:  # If there's a rule Y|X, this order is invalid
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def reorder_update(update, rules):
    """Reorder the pages in the update according to the rules."""
    # Create a directed graph from the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Separate rules and updates
    rules_section = []
    updates_section = []
    parsing_rules = True
    for line in lines:
        line = line.strip()
        if not line:
            parsing_rules = False
            continue
        if parsing_rules:
            rules_section.append(line)
        else:
            updates_section.append(line)

    # Parse rules
    rules = parse_rules(rules_section)

    # Process updates
    invalid_updates = []
    for update_line in updates_section:
        update = list(map(int, update_line.split(",")))
        if not is_valid_update(update, rules):
            invalid_updates.append(update)

    total_middle_sum = 0
    for update in invalid_updates:
        corrected_update = reorder_update(update, rules)
        total_middle_sum += find_middle_page(corrected_update)
    print(f"Total Middle Sum: {total_middle_sum}")

if __name__ == "__main__":
    main()
