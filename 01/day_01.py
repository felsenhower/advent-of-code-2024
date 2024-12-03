#!/usr/bin/env python3

import sys

def main() -> None:
    with open(sys.argv[1], "r") as f:
        lines = list(line.strip().split() for line in f)
    left, right = [sorted([int(line[i]) for line in lines]) for i in range(2)]
    result = sum(abs(l - r) for (l,r) in zip(left, right))
    print(result)

if __name__ == '__main__':
    main()
