def load_file(path: str) -> list[int]:
    with open(path, "r") as f:
        return [int(num) for num in f.read().strip().split()]


def blink(stones: list[int]) -> list[int]:
    stones_blink = []

    for stone in stones:
        if stone == 0:
            stones_blink.append(1)
        elif len(str(stone)) % 2 == 0:
            middle_idx = len(str(stone)) // 2
            stones_blink.append(int("".join([num for num in str(stone)[:middle_idx]])))
            stones_blink.append(int("".join([num for num in str(stone)[middle_idx:]])))
        else:
            stones_blink.append(stone * 2024)

    return stones_blink


if __name__ == "__main__":
    stones = load_file("task1_example_input")
    for i in range(25):
        stones = blink(stones)
    print(f"{len(stones) = }")
