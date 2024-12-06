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


def move_until_hash(level: list[str]) -> list[str]:
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

    while level[start_i + change_i][start_j + change_j] != "#":
        level[start_i][start_j] = "X"
        start_i += change_i
        start_j += change_j
        level[start_i][start_j] = direction


def patrol(level: list[str]) -> int:
    while 1:
        try:
            move_until_hash(level)
            guard_i, guard_j, dir = find_guard(level)
            if dir == "^":
                level[guard_i][guard_j] = ">"
            elif dir == ">":
                level[guard_i][guard_j] = "V"
            if dir == "V":
                level[guard_i][guard_j] = "<"
            if dir == "<":
                level[guard_i][guard_j] = "^"
        except IndexError:
            sum = 0
            for row in level:
                sum += row.count("X")
            return sum + 1


if __name__ == "__main__":
    level = load_file("task1_input")
    positions = patrol(level)
    print(f"{positions = }")
