#!/usr/bin/env python3

import sys

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = list(line.strip() for line in f)
    height = len(puzzle)
    width = len(puzzle[0])
    puzzle = (["." * (width + 6)] * 3) + [("..." + line + "...") for line in puzzle] + (["." * (width + 6)] * 3)
    total = 0
    for y in range(3, height + 3):
        for x in range(3, width + 3):
            N = [puzzle[y][x], puzzle[y-1][x], puzzle[y-2][x], puzzle[y-3][x]]
            S = [puzzle[y][x], puzzle[y+1][x], puzzle[y+2][x], puzzle[y+3][x]]
            W = [puzzle[y][x], puzzle[y][x-1], puzzle[y][x-2], puzzle[y][x-3]]
            E = [puzzle[y][x], puzzle[y][x+1], puzzle[y][x+2], puzzle[y][x+3]]
            NE = [puzzle[y][x], puzzle[y-1][x+1], puzzle[y-2][x+2], puzzle[y-3][x+3]]
            SE = [puzzle[y][x], puzzle[y+1][x+1], puzzle[y+2][x+2], puzzle[y+3][x+3]]
            SW = [puzzle[y][x], puzzle[y+1][x-1], puzzle[y+2][x-2], puzzle[y+3][x-3]]
            NW = [puzzle[y][x], puzzle[y-1][x-1], puzzle[y-2][x-2], puzzle[y-3][x-3]]
            total += ([N, S, W, E, NE, SE, SW, NW].count(["X","M","A","S"]))
    print(total)

if __name__ == '__main__':
    main()
