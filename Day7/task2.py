import itertools

OPERATORS = ["+", "*", "||"]


def load_file(path: str) -> dict[int, list[int]]:
    equations = {}
    with open(path, "r") as f:
        for line in f.readlines():
            equations[int(line[: line.index(":")])] = [
                int(num) for num in line[line.index(":") + 1 :].strip().split()
            ]
    return equations


def get_possibilities(numbers: list[int]):
    operators = list(itertools.product(OPERATORS, repeat=len(numbers) - 1))

    every_possibility = []
    for op in operators:
        possibility = []
        for i, number in enumerate(numbers[:-1]):
            possibility.append(number)
            possibility.append(op[i])
        possibility.append(numbers[-1])
        every_possibility.append(possibility)
    return every_possibility


def is_solvable(result: int, numbers: list[int]) -> bool:
    current_value = 0
    for i in range(0, len(numbers) - 2, 2):
        left = numbers[i]
        if current_value > 0:
            left = current_value
        op = numbers[i + 1]
        right = numbers[i + 2]
        if op == "||":
            current_value = int(f"{left}{right}")
        else:
            current_value = eval(f"{left} {op} {right}")
    if result == current_value:
        return True
    return False


def solve_equations(equations: dict[int, list[int]]) -> int:
    solvable_equations = 0
    i = 1
    for result, numbers in equations.items():
        print(f"{i}/{len(equations)}")
        skip = False
        for possibility in get_possibilities(numbers):
            if is_solvable(result, possibility):
                skip = True
                solvable_equations += result
            if skip:
                break
        i += 1
    return solvable_equations


if __name__ == "__main__":
    equations = load_file("task2_input")
    sum = solve_equations(equations)
    print(f"{sum = }")
