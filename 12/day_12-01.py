#!/usr/bin/env python3

import sys

def is_point_in_map(y: int, x: int, height: int, width: int) -> bool:
    if not (0 <= y < height):
        return False
    if not (0 <= x < width):
        return False
    return True

def get_neighbors(y: int, x: int, height: int, width: int) -> set[tuple[int,int]]:
    neighbors = [
        (y-1, x),
        (y, x-1), (y, x+1),
        (y+1, x),
    ]
    return {(y,x) for (y,x) in neighbors if is_point_in_map(y, x, height, width)}

def get_region(result, y: int, x: int, height: int, width: int, puzzle) -> set[tuple[int,int]]:
    result.add((y,x))
    plant = puzzle[y][x]
    neighbors = get_neighbors(y, x, height, width)
    neighbors = neighbors.difference(result)
    neighbors = {(y2,x2) for (y2,x2) in neighbors if puzzle[y2][x2] == plant}
    for (y3,x3) in neighbors:
        get_region(result, y3, x3, height, width, puzzle)
    return result

def get_area(region):
    return len(region)

def get_perimeter(region, height, width):
    perimeter = 0
    for (y,x) in region:
        neighbors = get_neighbors(y, x, height, width)
        neighbors.intersection_update(region)
        perimeter += (4 - len(neighbors))
    return perimeter

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [line.strip() for line in f]
    height = len(puzzle)
    width = len(puzzle[0])
    coordinates = {(y,x) for y in range(height) for x in range(width)}
    regions = []
    while True:
        try:
            (y,x) = coordinates.pop()
            region = get_region(set(), y, x, height, width, puzzle)
            coordinates.difference_update(region)
            regions.append(region)
        except KeyError:
            break
    price = 0
    for region in regions:
        area = get_area(region)
        perimeter = get_perimeter(region, height, width)
        price += (area * perimeter)
    print(price)
        
if __name__ == '__main__':
    main()
