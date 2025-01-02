#!/usr/bin/env python3

import sys
import re

RE_BUTTON_A = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
RE_BUTTON_B = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
RE_PRIZE = re.compile(r"Prize: X=(\d+), Y=(\d+)")

def multiply(scalar: int, vector: tuple[int,int]) -> tuple[int,int]:
    return (scalar * vector[0], scalar * vector[1])

def add(vec1: tuple[int,int], vec2: tuple[int,int]) -> tuple[int,int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def get_cost(num_a: int, num_b: int):
    return (num_a * 3) + (num_b)

def main() -> None:
    puzzle = []
    with open(sys.argv[1], "r") as f:
        button_a = None
        button_b = None
        prize = None
        for line in f:
            line = line.strip()
            if (m := RE_BUTTON_A.match(line)):
                button_a = (*(int(x) for x in m.groups()),)
            elif (m := RE_BUTTON_B.match(line)):
                button_b = (*(int(x) for x in m.groups()),)
            elif (m := RE_PRIZE.match(line)):
                prize = (*(int(x) for x in m.groups()),)
            else:
                puzzle.append((button_a, button_b, prize))
        puzzle.append((button_a, button_b, prize))
    result = 0
    for (button_a, button_b, prize) in puzzle:
        prize = add(prize, (10000000000000, 10000000000000))
        max_num_a = min(prize[0] // button_a[0], prize[1] // button_a[1])
        min_cost = None
        for num_a in range(max_num_a + 1):
            num_b = (prize[0] - (num_a * button_a[0])) // button_b[0]
            pos = add(multiply(num_a, button_a), multiply(num_b, button_b))
            if pos != prize:
                continue
            cost = get_cost(num_a, num_b)
            if min_cost is None or cost < min_cost:
                min_cost = cost
        if min_cost is not None:
            result += min_cost
    print(result)

if __name__ == '__main__':
    main()
