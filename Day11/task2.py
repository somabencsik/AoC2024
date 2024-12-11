def load_file(path: str) -> list[int]:
    with open(path, "r") as f:
        return [int(num) for num in f.read().strip().split()]


memory: dict[tuple[int, int], int] = {}


def blink(stone: int, blinks: int) -> list[int]:
    if blinks == 0:
        return 1

    if (stone, blinks) in memory:
        return memory[(stone, blinks)]

    value = 0
    if stone == 0:
        value += blink(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        m = len(str(stone)) // 2
        l = int(str(stone)[:m])
        r = int(str(stone)[m:])
        value += blink(l, blinks - 1) + blink(r, blinks - 1)
    else:
        value += blink(stone * 2024, blinks - 1)

    memory[(stone, blinks)] = value
    return value


if __name__ == "__main__":
    stones = load_file("task2_input")
    sum = 0
    for stone in stones:
        sum += blink(stone, 75)
    print(f"{sum = }")
