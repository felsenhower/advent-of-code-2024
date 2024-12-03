#!/usr/bin/env python3

import sys

def is_safe(report: list[int]) -> bool:
    sorted_report = sorted(report)
    if sorted_report != report and list(reversed(sorted_report)) != report:
        return False
    diffs = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
    return 1 <= min(diffs) and 3 >= max(diffs)

def is_actually_safe(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for i in range(len(report)):
        report2 = report.copy()
        del report2[i]
        if is_safe(report2):
            return True
    return False

def main() -> None:
    with open(sys.argv[1], "r") as f:
        lines = [line for line in f]
    reports = [[int(x) for x in line.strip().split()] for line in lines]
    result = sum(is_actually_safe(report) for report in reports)
    print(result)

if __name__ == '__main__':
    main()
