from copy import deepcopy


def load_file(path: str) -> list[str]:
    level = []
    with open(path, "r") as f:
        for line in f.readlines():
            level.append([char for char in line.strip()])
    return level


def find_guard(level: list[str]) -> tuple[int, int, str]:
    for i, row in enumerate(level):
        for j, char in enumerate(row):
            if char == "^" or char == ">" or char == "<" or char == "V":
                return (i, j, char)


def move_until_hash(level: list[str], previous_moves: dict[tuple, str]) -> bool | None:
    start_i, start_j, direction = find_guard(level)
    change_i, change_j = 0, 0
    if direction == "^":
        change_i = -1
    elif direction == ">":
        change_j = 1
    elif direction == "<":
        change_j = -1
    elif direction == "V":
        change_i = 1

    try:
        while (
            level[start_i + change_i][start_j + change_j] != "#"
            and level[start_i + change_i][start_j + change_j] != "O"
        ):
            if (start_i, start_j) in previous_moves and previous_moves[
                (start_i, start_j)
            ] == direction:
                return True
            level[start_i][start_j] = "X"
            previous_moves[(start_i, start_j)] = direction
            start_i += change_i
            start_j += change_j
            level[start_i][start_j] = direction
    except IndexError:
        level[start_i][start_j] = "X"
        raise IndexError

    if start_i + change_i < 0 or start_j + change_j < 0:
        raise IndexError


def patrol(level: list[str]) -> bool:
    current_level = level
    previous_moves = {}
    while 1:
        try:
            res = move_until_hash(current_level, previous_moves)
            if res:
                return True
            guard_i, guard_j, dir = find_guard(current_level)
            if dir == "^":
                current_level[guard_i][guard_j] = ">"
            elif dir == ">":
                current_level[guard_i][guard_j] = "V"
            if dir == "V":
                current_level[guard_i][guard_j] = "<"
            if dir == "<":
                current_level[guard_i][guard_j] = "^"
        except IndexError:
            return False
    return False


if __name__ == "__main__":
    level = load_file("task2_input")
    level_test = deepcopy(level)
    patrol(level_test)
    possible_obstructions = []
    for i, row in enumerate(level_test):
        for j, char in enumerate(row):
            if char == "X":
                possible_obstructions.append((i, j))
    total_possible_obstructions = len(possible_obstructions)

    tries = 1
    sum = 0
    for i, row in enumerate(level):
        for j, char in enumerate(row):
            if (i, j) not in possible_obstructions:
                continue

            new_level = deepcopy(level)

            if char == ".":
                new_level[i][j] = "O"
            else:
                continue

            if patrol(new_level):
                sum += 1
            new_level[i][j] = "."
            print(f"{tries}/{total_possible_obstructions}")
            tries += 1

    print(f"{sum = }")
