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


def get_every_antinode_on_vector(
    start_i: int, start_j: int, change_i: int, change_j: int, max_i: int, max_j: int
) -> list[tuple[int, int]]:
    antinodes = []
    new_point = (start_i, start_j)
    while (
        new_point[0] + change_i >= 0
        and new_point[0] + change_i < max_j
        and new_point[1] + change_j >= 0
        and new_point[1] + change_j < max_i
    ):
        antinodes.append(new_point)
        new_point = (new_point[0] + change_i, new_point[1] + change_j)
        antinodes.append(new_point)
    new_point = (start_i, start_j)
    while (
        new_point[0] - change_i >= 0
        and new_point[0] - change_i < max_j
        and new_point[1] - change_j >= 0
        and new_point[1] - change_j < max_i
    ):
        antinodes.append(new_point)
        new_point = (new_point[0] - change_i, new_point[1] - change_j)
        antinodes.append(new_point)
    return antinodes


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
                antinodes_on_vector = get_every_antinode_on_vector(
                    point1[0], point1[1], x_diff, y_diff, max_i, max_j
                )
                for antinode in antinodes_on_vector:
                    if antinode not in antinodes:
                        antinodes.append(antinode)
    return len(antinodes)


if __name__ == "__main__":
    city = load_file("task2_input")
    antennas = get_antennas(city)
    antinodes = get_antinodes(antennas, len(city), len(city[0]))
    print(f"{antinodes = }")
