def load_file(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.readlines()

        for i, line in enumerate(data):
            data[i] = line.strip()

    return data


def check_lines(lines: list[str]) -> int:
    sum = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + 2 < len(lines) and j + 2 < len(lines[i]):
                if (
                    lines[i][j] == "M"
                    and lines[i + 1][j + 1] == "A"
                    and lines[i + 2][j + 2] == "S"
                    and lines[i][j + 2] == "M"
                    and lines[i + 2][j] == "S"
                ):
                    sum += 1
                if (
                    lines[i][j] == "S"
                    and lines[i + 1][j + 1] == "A"
                    and lines[i + 2][j + 2] == "M"
                    and lines[i][j + 2] == "S"
                    and lines[i + 2][j] == "M"
                ):
                    sum += 1
                if (
                    lines[i][j] == "S"
                    and lines[i + 1][j + 1] == "A"
                    and lines[i + 2][j + 2] == "M"
                    and lines[i][j + 2] == "M"
                    and lines[i + 2][j] == "S"
                ):
                    sum += 1
                if (
                    lines[i][j] == "M"
                    and lines[i + 1][j + 1] == "A"
                    and lines[i + 2][j + 2] == "S"
                    and lines[i][j + 2] == "S"
                    and lines[i + 2][j] == "M"
                ):
                    sum += 1

    return sum


if __name__ == "__main__":
    original_lines = load_file("task2_input")
    result = check_lines(original_lines)
    print(f"{result = }")
