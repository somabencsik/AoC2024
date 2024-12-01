def load_file(path: str) -> tuple[list[int], list[int]]:
    left, right = [], []

    with open(path, "r") as f:
        for line in f.readlines():
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    return left, right


def get_next_distance(left: list[int], right: list[int]) -> int:
    min_l = min(left)
    min_r = min(right)

    left.remove(min_l)
    right.remove(min_r)

    d = abs(min_l - min_r)
    return d


def loop(left: list[int], right: list[int]) -> int:
    total_distance = 0
    while len(left) > 0:
        total_distance += get_next_distance(left, right)
    return total_distance


if __name__ == "__main__":
    left, right = load_file("task1_input")
    total_distance = loop(left, right)
    print(f"{total_distance = }")
