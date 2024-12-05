def load_file(path: str) -> tuple[dict[int, tuple[int, int]], list[list[int]]]:
    rules = {}
    updates = []
    empty_line = False
    with open(path, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if line == "":
                empty_line = True
                continue

            if not empty_line:
                rules[i] = (int(line.split("|")[0]), int(line.split("|")[1]))
                continue

            updates.append([int(l) for l in line.split(",")])

    return rules, updates


def check_update(rules: dict[int, tuple[int, int]], update: list[int]):
    for i, left in enumerate(update[:-1]):
        for right in update[i + 1 :]:
            rule_to_find = (right, left)
            for _, rule in rules.items():
                if rule != rule_to_find:
                    continue
                return False
    return True


def check_updates(rules: dict[int, tuple[int, int]], updates: list[list[int]]) -> int:
    sum = 0
    for update in updates:
        if check_update(rules, update):
            sum += update[len(update) // 2]
    return sum


if __name__ == "__main__":
    rules, updates = load_file("task1_input")
    correct_updates = check_updates(rules, updates)
    print(f"{correct_updates = }")
