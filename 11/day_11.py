#!/usr/bin/env python3

import sys

def blink(stones: list[int]) -> list[int]:
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        else:
            stone_str = str(stone)
            stone_str_len = len(stone_str)
            if stone_str_len % 2 == 0:
                new_length = stone_str_len // 2
                left = int(stone_str[:new_length])
                right = int(stone_str[new_length:])
                result += [left, right]
            else:
                result.append(stone * 2024)
    return result

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [int(x) for x in f.read().strip().split()]
    num_blinks = int(sys.argv[2])
    print()
    for i in range(num_blinks):
        puzzle = blink(puzzle)
        print(f"\r{i+1} / {num_blinks}", end="")
    print()
    print(len(puzzle))


if __name__ == '__main__':
    main()
