def load_file(path: str) -> list[str]:
    with open(path, "r") as file:
        return [char for char in file.read()]


def get_files(disk_map: list[str]) -> list[str]:
    files = []

    current_id = 0
    for i, id in enumerate(disk_map):
        id = int(id)
        if i % 2 == 0:
            files += [f"{current_id}"] * id
            current_id += 1
            continue
        files += ["."] * id

    return files


def defragment_files(files: list[str]) -> None:
    free_spaces = {}
    start_idx = 0
    while start_idx < len(files):
        try:
            while files[start_idx] != ".":
                start_idx += 1
        except IndexError:
            break
        space = 0
        for i, file in enumerate(files[start_idx:]):
            if file == ".":
                space += 1
                continue
            break
        free_spaces[start_idx] = space
        start_idx += space

    right_ptr = len(files) - 1
    while right_ptr >= 0:
        while files[right_ptr] == ".":
            right_ptr -= 1
        num = files[right_ptr]
        num_space = files.count(num)
        for i, left_space in free_spaces.items():
            if left_space < num_space:
                continue
            if i > right_ptr:
                continue
            for j in range(num_space):
                files[i + j], files[right_ptr - j] = files[right_ptr - j], files[i + j]
            if free_spaces[i] - num_space > 0:
                free_spaces[i + num_space] = free_spaces[i] - num_space
                del free_spaces[i]
            else:
                free_spaces[i] = free_spaces[i] - num_space
            free_spaces = dict(sorted(free_spaces.items()))
            break
        right_ptr -= num_space


def get_filesystem_checksum(defraged_files: list[str]) -> int:
    sum = 0
    for i, file in enumerate(defraged_files):
        if file == ".":
            continue
        sum += i * int(file)
    return sum


if __name__ == "__main__":
    disk_map = load_file("task2_input")
    files = get_files(disk_map)
    defragment_files(files)
    filesystem_checksum = get_filesystem_checksum(files)
    print(f"{filesystem_checksum = }")
