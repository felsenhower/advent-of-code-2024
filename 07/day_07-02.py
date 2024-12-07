#!/usr/bin/env python3

import sys
import itertools
from functools import lru_cache

@lru_cache(maxsize=None)
def get_operator_possibilities(num_operators: int):
    return list(itertools.product("*+|", repeat=num_operators))
    
def calculate(operands, operators) -> int:
    operands = list(operands)
    result = operands[0]
    for (operand, operator) in zip(operands[1:], operators):
        if operator == "*":
            result *= operand
        elif operator == "+":
            result += operand
        elif operator == "|":
            result = int(str(result)+str(operand))
    return result

def is_valid(result, operands) -> bool:
    num_operators = len(operands) - 1
    for operators in get_operator_possibilities(num_operators):
        if result == calculate(operands, operators):
            return True
    return False

def main() -> None:
    with open(sys.argv[1], "r") as f:
        puzzle = [(result, (*operands,)) for (result, *operands) in [[int(x) for x in line.strip().replace(":","").split()] for line in f]]
    total = 0
    for (result, operands) in puzzle:
        if is_valid(result, operands):
            total += result
    print(total)

if __name__ == '__main__':
    main()
