#!/usr/bin/env python3

import sys
import itertools

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [line.strip() for line in f]
    height = len(puzzle)
    width = len(puzzle[0])
    antenna_positions = set()
    antenna_positions_by_freq = dict()
    for (y,line) in enumerate(puzzle):
        for (x, freq) in enumerate(line):
            if freq == ".":
                continue
            antenna_positions.add((y,x,))
            if freq not in antenna_positions_by_freq:
                antenna_positions_by_freq[freq] = []
            antenna_positions_by_freq[freq].append((y,x,))
    antinodes = set()
    for (freq, positions) in antenna_positions_by_freq.items():
        for (first, second) in itertools.permutations(positions, 2):
            antinode = ((2 * second[0] - first[0]), (2 * second[1] - first[1]))
            is_in_map = ((antinode[0] >= 0) and (antinode[0] < height) and (antinode[1] >= 0) and (antinode[1] < width))
            if is_in_map:
                antinodes.add(antinode)
    print(len(antinodes))

if __name__ == '__main__':
    main()
