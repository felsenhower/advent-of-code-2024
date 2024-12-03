#!/usr/bin/env python3

import sys
import re

re_mul = re.compile(r"(?:mul\((\d+),(\d+)\))|(?:do\(\))|(?:don't\(\))")

def main() -> None:
    with open(sys.argv[1], "r") as f:
        memory = f.read().strip()
    do = True
    total = 0
    for m in re_mul.finditer(memory):
        if m[0] == "do()":
            do = True
        elif m[0] == "don't()":
            do = False
        elif do:
            total += int(m[1]) * int(m[2])
    print(total)


if __name__ == '__main__':
    main()
