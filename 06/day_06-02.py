#!/usr/bin/env python3

import sys
import re
from time import sleep

RE_GUARD = re.compile(r"\^|v|\>|\<")

def find_guard(puzzle: list[str]) -> tuple[str,int,int]:
    for (y, line) in enumerate(puzzle):
        if m := RE_GUARD.search(line):
            x = m.span()[0]
            guard = m[0]
            return (guard, (y, x))
    return None

def get_position_in_front_of_guard(guard: str, y: int, x: int) -> tuple[int,int]:
    assert guard in "^v<>"
    if guard == "^":
        return ((y - 1), x)
    if guard == "v":
        return ((y + 1), x)
    if guard == ">":
        return (y, (x + 1))
    if guard == "<":
        return (y, (x - 1))

def get_turned_guard_marker(guard: str) -> str:
    assert guard in "^v<>"
    if guard == "^":
        return ">"
    if guard == "v":
        return "<"
    if guard == ">":
        return "v"
    if guard == "<":
        return "^"

def is_obstacle_in_front(puzzle: list[str]) -> bool:
    guard, (y, x) = find_guard(puzzle)
    y_front, x_front = get_position_in_front_of_guard(guard, y, x)
    return puzzle[y_front][x_front] == "#"

def is_position_in_map(x: int, y: int, puzzle: list[str]) -> bool:
    return (y >= 0) and (y < len(puzzle)) and (x >= 0) and (x < len(puzzle[0]))

def is_wall_in_front(puzzle: list[str]) -> bool:
    guard, (y, x) = find_guard(puzzle)
    y_front, x_front = get_position_in_front_of_guard(guard, y, x)
    return not is_position_in_map(y_front, x_front, puzzle)

def go_forward(puzzle: list[str]) -> list[str]:
    guard, (y, x) = find_guard(puzzle)
    y_new, x_new = get_position_in_front_of_guard(guard, y, x)
    listified = [list(line) for line in puzzle]
    listified[y][x] = "."
    listified[y_new][x_new] = guard
    return ["".join(line) for line in listified]

def turn_right(puzzle: list[str]) -> list[str]:
    guard, (y, x) = find_guard(puzzle)
    new_marker = get_turned_guard_marker(guard)
    listified = [list(line) for line in puzzle]
    listified[y][x] = new_marker
    return ["".join(line) for line in listified]

def print_puzzle(puzzle: list[str]):
    for line in puzzle:
        print(line)

def place_obstacle(puzzle: list[str], y: int, x: int) -> list[str]:
    assert is_position_in_map(x,y,puzzle)
    listified = [list(line) for line in puzzle]
    listified[y][x] = "#"    
    return ["".join(line) for line in listified]

def is_guard_stuck_in_loop(puzzle: list[str]):
    path = set()
    while True:
        marker = find_guard(puzzle)
        if marker in path:
            return True
        path.add(marker)
        if is_wall_in_front(puzzle):
            break
        if is_obstacle_in_front(puzzle):
            puzzle = turn_right(puzzle)
        else:
            puzzle = go_forward(puzzle)
        if False:
            print_puzzle(puzzle)
            print("---")
            sleep(0.1)
    return False

def get_visited_positions(puzzle) -> set[tuple[int,int]]:
    positions = set()
    while True:
        _, guard_pos = find_guard(puzzle)
        positions.add(guard_pos)
        if is_wall_in_front(puzzle):
            break
        if is_obstacle_in_front(puzzle):
            puzzle = turn_right(puzzle)
        else:
            puzzle = go_forward(puzzle)
        if False:
            print_puzzle(puzzle)
            print("---")
            sleep(0.1)
    return positions
    
def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [line.strip() for line in f]
    positions = get_visited_positions(puzzle)
    _, start_pos = find_guard(puzzle)
    positions.remove(start_pos)
    positions = list(positions)
    total = 0
    print()
    for (i, (y, x)) in enumerate(positions):
        total += is_guard_stuck_in_loop(place_obstacle(puzzle, y, x))
        print(f"\rTried position {i+1} / {len(positions)}: ({y},{x}). Found {total} so far.          ", end="")
    print()
    print(total)
    
if __name__ == '__main__':
    main()
