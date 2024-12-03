import re


def load_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def check_memory(memory: str) -> int:
    multiplies = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)

    result = 0
    for mulitply in multiplies:
        left = mulitply[4 : mulitply.index(",")]
        right = mulitply[mulitply.index(",") + 1 : -1]
        result += int(left) * int(right)

    return result


if __name__ == "__main__":
    memory = load_file("task1_input")
    result = check_memory(memory)
    print(f"{result = }")
