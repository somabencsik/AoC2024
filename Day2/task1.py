def load_file(path: str) -> list[list[int]]:
    reports = []

    with open(path, "r") as f:
        for line in f.readlines():
            report = []
            [report.append(int(level)) for level in line.split()]
            reports.append(report)

    return reports


def check_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        skip = False

        increasing = True if report[0] - report[1] < 0 else False
        for i in range(0, len(report) - 1):
            d = report[i] - report[i + 1]

            if d == 0:
                skip = True
                break
            elif d < 0 and not increasing:
                skip = True
                break
            elif d > 0 and increasing:
                skip = True
                break
            elif abs(d) > 3:
                skip = True
                break

        if skip:
            continue

        safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    reports = load_file("task1_input")
    safe_reports = check_safe_reports(reports)
    print(f"{safe_reports = }")
