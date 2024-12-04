def load_file(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.readlines()

        for i, line in enumerate(data):
            data[i] = line.strip()

    return data


def check_lines(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        start_idx = 0
        while line.find("XMAS", start_idx) != -1:
            sum += 1
            start_idx = line.find("XMAS", start_idx) + 1

        start_idx = 0
        while line.find("SAMX", start_idx) != -1:
            sum += 1
            start_idx = line.find("SAMX", start_idx) + 1

    return sum


def rotate_by_90(lines: list[str]) -> list[str]:
    new_lines = []
    for i in range(len(lines)):
        new_line = ""
        for j in range(len(lines[i])):
            new_line += lines[j][i]
        new_lines.append(new_line)

    return new_lines


def check_diagonal(lines: list[str]) -> int:
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + 3 < len(lines) and j + 3 < len(lines[i]):
                if (
                    lines[i][j] == "X"
                    and lines[i + 1][j + 1] == "M"
                    and lines[i + 2][j + 2] == "A"
                    and lines[i + 3][j + 3] == "S"
                ):
                    sum += 1

            if i - 3 >= 0 and j - 3 >= 0:
                if (
                    lines[i][j] == "X"
                    and lines[i - 1][j - 1] == "M"
                    and lines[i - 2][j - 2] == "A"
                    and lines[i - 3][j - 3] == "S"
                ):
                    sum += 1

            if i - 3 >= 0 and j + 3 < len(lines[i]):
                if (
                    lines[i][j] == "X"
                    and lines[i - 1][j + 1] == "M"
                    and lines[i - 2][j + 2] == "A"
                    and lines[i - 3][j + 3] == "S"
                ):
                    sum += 1

            if i + 3 < len(lines) and j - 3 >= 0:
                if (
                    lines[i][j] == "X"
                    and lines[i + 1][j - 1] == "M"
                    and lines[i + 2][j - 2] == "A"
                    and lines[i + 3][j - 3] == "S"
                ):
                    sum += 1

    return sum


if __name__ == "__main__":
    original_lines = load_file("task1_input")
    result = check_lines(original_lines)

    lines_90 = rotate_by_90(original_lines)
    result += check_lines(lines_90)

    result += check_diagonal(original_lines)

    print(f"{result = }")
