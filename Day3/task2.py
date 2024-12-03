import re


def load_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def next_instruction(string: str, sub_string: str, start_idx: int) -> int | None:
    try:
        return string.index(sub_string, start_idx)
    except ValueError:
        return None


def find_instructions(memory: str) -> list[tuple[True, int]]:
    instructions = []

    start_idx = 0
    while next_instruction(memory, "do()", start_idx) is not None:
        instructions.append((True, memory.index("do()", start_idx)))
        start_idx = memory.index("do()", start_idx) + 3

    start_idx = 0
    while next_instruction(memory, "don't()", start_idx) is not None:
        instructions.append((False, memory.index("don't()", start_idx)))
        start_idx = memory.index("don't()", start_idx) + 3

    instructions = sorted(instructions, key=lambda l: l[1])

    return instructions


def check_memory(memory: str) -> int:
    multiplies = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)

    instructions = find_instructions(memory)
    used_indexes = []

    result = 0
    for mulitply in multiplies:
        left = mulitply[4 : mulitply.index(",")]
        right = mulitply[mulitply.index(",") + 1 : -1]

        global_index = memory.index(f"mul({left},{right})")
        if global_index in used_indexes:
            global_index = memory.index(f"mul({left},{right})", global_index + 8)

        used_indexes.append(global_index)

        do = True
        for instruction in instructions:
            if instruction[1] > global_index:
                continue
            if instruction[1] < global_index:
                do = instruction[0]

        if do:
            result += int(left) * int(right)

    return result


if __name__ == "__main__":
    memory = load_file("task2_input")
    result = check_memory(memory)
    print(f"{result = }")
