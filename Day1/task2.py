def load_file(path: str) -> tuple[list[int], list[int]]:
    left, right = [], []

    with open(path, "r") as f:
        for line in f.readlines():
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    return left, right


def get_right_numbers(right: list[int]) -> dict[int, int]:
    occurrence = {}

    for r in right:
        if r not in occurrence:
            occurrence[r] = 1
            continue
        occurrence[r] += 1

    return occurrence


def loop(left: list[int], right: list[int]) -> int:
    right_map = get_right_numbers(right)
    similarity_score = 0

    for l in left:
        if l not in right_map:
            continue
        similarity_score += l * right_map[l]

    return similarity_score


if __name__ == "__main__":
    left, right = load_file("task2_input")
    similarity_score = loop(left, right)
    print(f"{similarity_score = }")
