#!/usr/bin/env python3

import sys

def is_update_ok(update: list[int], rules: list[list[int]]) -> bool:
    for rule in rules:
        try:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
        except ValueError:
            continue
    return True

def middle_number(update: list[int]) -> int:
    return update[len(update) // 2]

def main() -> None:
    with open(sys.argv[1], "r") as f:
        lines = f.read().strip().split("\n")
    gap = lines.index("")
    rules = [[int(x) for x in line.split("|")] for line in lines[:gap]]
    updates = [[int(x) for x in line.split(",")] for line in lines[gap+1:]]
    print(sum(middle_number(update) for update in updates if is_update_ok(update, rules)))

if __name__ == '__main__':
    main()
