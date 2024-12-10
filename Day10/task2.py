def load_file(path: str) -> list[list[str]]:
    topographic_map = []
    with open(path, "r") as f:
        for line in f.readlines():
            topographic_map.append([int(num) for num in line.strip()])
    return topographic_map


def find_starts(topographic_map: list[list[str]]) -> list[tuple[int, int]]:
    starts = []
    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[i])):
            if topographic_map[i][j] != 0:
                continue
            starts.append((i, j))
    return starts


def find_steps(start: tuple[int, int]) -> list[tuple[int, int]]:
    paths = []

    i = start[0]
    j = start[1]
    paths.append((i - 1, j))
    paths.append((i + 1, j))
    paths.append((i, j - 1))
    paths.append((i, j + 1))

    return paths


def find_trail(topographic_map: list[list[str]], start: tuple[int, int]) -> bool:
    result = []

    def backtrack(topographic_map: list[list[str]], start: tuple[int, int]):
        start_i = start[0]
        start_j = start[1]
        if topographic_map[start_i][start_j] == 9:
            result.append((start_i, start_j, topographic_map[start_i][start_j]))
            return

        for step in find_steps(start):
            step_i = step[0]
            step_j = step[1]

            if (
                step_i >= 0
                and step_i < len(topographic_map)
                and step_j >= 0
                and step_j < len(topographic_map[step_i])
                and topographic_map[step_i][step_j]
                == topographic_map[start_i][start_j] + 1
            ):
                result.append((step_i, step_j, topographic_map[step_i][step_j]))
                backtrack(topographic_map, step)

    backtrack(topographic_map, start)
    return result


def find_trails(topographic_map: list[list[str]], starts: list[tuple[int, int]]) -> int:
    sum = 0
    for start in starts:
        paths = {}
        res = find_trail(topographic_map, start)
        for path in res:
            if path[2] not in paths:
                paths[path[2]] = []
            paths[path[2]].append((path[0], path[1]))
        sum += len(paths[9]) // 2
    return sum


if __name__ == "__main__":
    topographic_map = load_file("task2_input")
    starts = find_starts(topographic_map)
    trails = find_trails(topographic_map, starts)
    print(f"{trails = }")
