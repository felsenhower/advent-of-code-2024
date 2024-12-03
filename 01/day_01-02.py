#!/usr/bin/env python3

import sys

def main() -> None:
    with open(sys.argv[1], "r") as f:
        lines = list(line.strip().split() for line in f)
    left, right = [([int(line[i]) for line in lines]) for i in range(2)]
    similarities = [right.count(l) for l in left]
    result = sum((l * s) for (l,s) in zip(left, similarities))
    print(result)

if __name__ == '__main__':
    main()
