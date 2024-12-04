#!/usr/bin/env python3

import sys

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = list(line.strip() for line in f)
    height = len(puzzle)
    width = len(puzzle[0])
    total = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if puzzle[y][x] != "A":
                continue
            if not [puzzle[y-1][x-1], puzzle[y+1][x+1]] in [["M","S"],["S","M"]]:
                continue
            if not [puzzle[y-1][x+1], puzzle[y+1][x-1]] in [["M","S"],["S","M"]]:
                continue
            total += 1
    print(total)

if __name__ == '__main__':
    main()
