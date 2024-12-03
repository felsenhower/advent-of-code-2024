#!/usr/bin/env python3

import sys
import re

re_mul = re.compile(r"mul\((\d+),(\d+)\)")

def main() -> None:
    with open(sys.argv[1], "r") as f:
        memory = f.read().strip()
    result = sum((int(m[1]) * int(m[2])) for m in re_mul.finditer(memory))
    print(result)


if __name__ == '__main__':
    main()
