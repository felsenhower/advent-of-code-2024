#!/usr/bin/env python3

import sys

def get_ids(puzzle):
    current_id = 0
    result = []
    is_file = True
    for x in puzzle:
        id = [current_id] if is_file else [None]
        id *= x
        result += id
        if is_file:
            current_id += 1
        is_file = not is_file
    return result

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [int(x) for x in f.read().strip()]
    ids = get_ids(puzzle)
    while True:
        try:
            first_none_index = ids.index(None)
        except ValueError:
            break
        last_non_none = None
        while not last_non_none:
            last_non_none = ids.pop()
        try:
            ids[first_none_index] = last_non_none
        except IndexError:
            ids.append(last_non_none)
            break
    result = sum((pos * id) for (pos,id) in enumerate(ids))
    print(result)

if __name__ == '__main__':
    main()
