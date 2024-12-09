#!/usr/bin/env python3

import sys

def get_ids(puzzle):
    current_id = 0
    result = []
    sublists = []
    is_file = True
    for x in puzzle:
        id = [current_id] if is_file else [None]
        id *= x
        result += id
        if is_file:
            sublists.append(id)
            current_id += 1
        is_file = not is_file
    return result, sublists

def find_sublist(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    for i in range(haystack_len - needle_len + 1):
        position = slice(i, (i + needle_len))
        sublist = haystack[position]
        if sublist == needle:
            return position
    return None

def print_ids(ids):
    result = ""
    for x in ids:
        if x is not None:
            result += str(x)
        else:
            result += "."
    return result

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [int(x) for x in f.read().strip()]
    ids, sublists = get_ids(puzzle)
    for sublist in reversed(sublists[1:]):
        free_space = [None] * len(sublist)
        old_position = find_sublist(ids, sublist)
        new_position = find_sublist(ids, free_space)
        if not new_position or new_position.start >= old_position.start:
            continue
        ids[new_position] = sublist
        ids[old_position] = free_space
    total = 0
    current_index = 0
    for id in ids:
        if id is not None:
            total += current_index * id
        current_index += 1
    print(total)

if __name__ == '__main__':
    main()
