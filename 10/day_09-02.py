#!/usr/bin/env python3

import sys

def get_neighbors(pos: tuple[int, int], height: int, width: int) -> set[tuple[int,int]]:
    result = set()
    y, x = pos
    if y > 0:
        result.add((y - 1, x))
    if y < (height - 1):
        result.add((y + 1, x))
    if x > 0:
        result.add((y, x - 1))
    if x < (width - 1):
        result.add((y, x + 1))
    return result

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [[x for x in line.strip()] for line in f]
    elevation_positions = [set() for _ in range(10)]
    height = len(puzzle)
    width = len(puzzle[0])
    for (y, line) in enumerate(puzzle):
        for (x, char) in enumerate(line):
            if char != ".":
                elevation_positions[int(char)].add((y,x,))
    trailheads = elevation_positions[0]
    total = 0
    for start_position in trailheads:
        current_positions = [start_position]
        for step in range(1,10):
            neighbors = []
            for pos in current_positions:
                neighbors += get_neighbors(pos, height, width).intersection(elevation_positions[step])
            current_positions = neighbors
        total += len(current_positions)
    print(total)

if __name__ == '__main__':
    main()
