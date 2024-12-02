def load_file(path: str) -> list[list[int]]:
    reports = []

    with open(path, "r") as f:
        for line in f.readlines():
            report = []
            [report.append(int(level)) for level in line.split()]
            reports.append(report)

    return reports


def check_increasing(levels: list[int]) -> bool:
    for i in range(0, len(levels) - 1):
        d = levels[i] - levels[i + 1]
        if d == 0:
            continue
        elif d < 0:
            return True
        elif d > 0:
            return False


def get_unsafe_reports(reports: list[list[int]]) -> int:
    unsafe_reports = []

    for report in reports:
        levels = []
        skip = False

        increasing = check_increasing(report)
        for i in range(0, len(report) - 1):
            d = report[i] - report[i + 1]

            levels.append(report[i])

            if (
                (d == 0)
                or (d < 0 and not increasing)
                or (d > 0 and increasing)
                or (abs(d) > 3)
            ):
                skip = True

        levels.append(report[i + 1])

        if not skip:
            continue

        unsafe_reports.append(levels)

    return unsafe_reports


def check_report(report: list[int]):
    increasing = check_increasing(report)
    for i in range(0, len(report) - 1):
        d = report[i] - report[i + 1]

        if (
            (d == 0)
            or (d < 0 and not increasing)
            or (d > 0 and increasing)
            or (abs(d) > 3)
        ):
            return False
    return True


if __name__ == "__main__":
    reports = load_file("task2_input")
    safe_reports = 0
    for report in reports:
        safe_reports += 1 if check_report(report) else 0
    print(f"{safe_reports = }")
    unsafe_reports = get_unsafe_reports(reports)
    for report in unsafe_reports:
        if any(
            [check_report(report[:i] + report[i + 1 :]) for i in range(len(report))]
        ):
            safe_reports += 1
    print(f"{safe_reports = }")
