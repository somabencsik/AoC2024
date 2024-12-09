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


def get_defraged_files(files: list[str]) -> list[str]:
    defraged_files = []

    for file in files[: len(files) - files.count(".")]:
        next_right = None
        if file == ".":
            for i, f in enumerate(files[::-1]):
                if f == ".":
                    continue
                next_right = f
                files = files[: -i - 1]
                break
            defraged_files += [next_right]
            continue
        defraged_files += [file]

    return defraged_files


def get_filesystem_checksum(defraged_files: list[str]) -> int:
    sum = 0
    for i, file in enumerate(defraged_files):
        if file == ".":
            break
        sum += i * int(file)
    return sum


if __name__ == "__main__":
    disk_map = load_file("task1_input")
    files = get_files(disk_map)
    defraged_files = get_defraged_files(files) + ["."] * files.count(".")
    filesystem_checksum = get_filesystem_checksum(defraged_files)
    print(f"{filesystem_checksum = }")
