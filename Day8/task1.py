def load_file(path: str) -> list[list[str]]:
    city = []
    with open(path, "r") as f:
        for line in f.readlines():
            city.append(line.strip())
    return city


def get_antennas(city: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    antennas = {}
    for i in range(len(city)):
        for j in range(len(city[i])):
            antenna = city[i][j]
            if antenna == ".":
                continue
            if antenna not in antennas:
                antennas[antenna] = []
            antennas[antenna].append((i, j))
    return antennas


def get_antinodes(
    antennas: dict[str, list[tuple[int, int]]], max_i: int, max_j: int
) -> int:
    antinodes = []
    for _, antenna in antennas.items():
        for i in range(len(antenna) - 1):
            for j in range(i + 1, len(antenna)):
                point1 = antenna[i]
                point2 = antenna[j]
                x_diff = point1[0] - point2[0]
                y_diff = point1[1] - point2[1]
                new_point = (point1[0] + x_diff, point1[1] + y_diff)
                if (
                    new_point[0] < max_i
                    and new_point[0] >= 0
                    and new_point[1] < max_j
                    and new_point[1] >= 0
                ):
                    if new_point[0] == point2[0] and new_point[1] == point2[1]:
                        ...
                    else:
                        if new_point not in antinodes:
                            antinodes.append(new_point)
                new_point = (point1[0] - x_diff, point1[1] - y_diff)
                if (
                    new_point[0] < max_i
                    and new_point[0] >= 0
                    and new_point[1] < max_j
                    and new_point[1] >= 0
                ):
                    if new_point[0] == point2[0] and new_point[1] == point2[1]:
                        ...
                    else:
                        if new_point not in antinodes:
                            antinodes.append(new_point)

                new_point = (point2[0] + x_diff, point2[1] + y_diff)
                if (
                    new_point[0] < max_i
                    and new_point[0] >= 0
                    and new_point[1] < max_j
                    and new_point[1] >= 0
                ):
                    if new_point[0] == point1[0] and new_point[1] == point1[1]:
                        ...
                    else:
                        if new_point not in antinodes:
                            antinodes.append(new_point)
                new_point = (point2[0] - x_diff, point2[1] - y_diff)
                if (
                    new_point[0] < max_i
                    and new_point[0] >= 0
                    and new_point[1] < max_j
                    and new_point[1] >= 0
                ):
                    if new_point[0] == point1[0] and new_point[1] == point1[1]:
                        ...
                    else:
                        if new_point not in antinodes:
                            antinodes.append(new_point)
    return len(antinodes)


if __name__ == "__main__":
    city = load_file("task1_input")
    antennas = get_antennas(city)
    antinodes = get_antinodes(antennas, len(city), len(city[0]))
    print(f"{antinodes = }")
