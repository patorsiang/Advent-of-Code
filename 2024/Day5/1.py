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
    total_middle_sum = 0
    for update_line in updates_section:
        update = list(map(int, update_line.split(",")))
        if is_valid_update(update, rules):
            total_middle_sum += find_middle_page(update)

    print(f"Total Middle Sum: {total_middle_sum}")

if __name__ == "__main__":
    main()
