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


def check_update(
    rules: dict[int, tuple[int, int]], update: list[int], pos=False
) -> bool:
    for i, left in enumerate(update[:-1]):
        for j, right in enumerate(update[i + 1 :]):
            rule_to_find = (right, left)
            for _, rule in rules.items():
                if rule != rule_to_find:
                    continue
                if not pos:
                    return False
                else:
                    return False, i, i + j + 1
    if not pos:
        return True
    else:
        return True, None, None


def check_updates(rules: dict[int, tuple[int, int]], updates: list[list[int]]) -> int:
    sum = 0
    for update in updates:
        update = reorder_wrong_update(rules, update)
        if check_update(rules, update):
            sum += update[len(update) // 2]
    return sum


def get_wrong_updates(
    rules: dict[int, tuple[int, int]], updates: list[list[int]]
) -> list[int]:
    wrong_updates = []
    for update in updates:
        if not check_update(rules, update):
            wrong_updates.append(update)
    return wrong_updates


def reorder_wrong_update(
    rules: dict[int, tuple[int, int]], update: list[int]
) -> list[int]:
    while not check_update(rules, update, pos=True)[0]:
        right, i, j = check_update(rules, update, pos=True)
        if not right:
            update[i], update[j] = update[j], update[i]
    return update


if __name__ == "__main__":
    rules, updates = load_file("task2_input")
    wrong_updates = get_wrong_updates(rules, updates)
    correct_updates = check_updates(rules, wrong_updates)
    print(f"{correct_updates = }")
