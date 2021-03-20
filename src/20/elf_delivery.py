""" 
Author: Darren
Date: 19/03/2021

Solving https://adventofcode.com/2015/day/20

Infinite elves deliver to infinite houses numbered sequentially.
Each elf is assigned a number and a progression.
Elf e visits houses eh. E.g.
    elf 1 visits 1, 2, 3, 4, 5, 6, 7, 8, 9 ...
    elf 2 visits    2     4     6     8    ...
    elf 3 visits       3        6        9 ...

At each house h, elf e delivers 10x presents.  Thus:
house 1 gets 10, house 2 gets 30, house 3 gets 40...

Solution:

Part 1:
    House 6 is visted by elves 1, 2, 3, and 6.
    Thus, we must determine all factors of 6.
    Return these factors, and multiple each by 10.

Part 2:
    Now we need to count visits by each elf.
    No elf visits more than 50 houses.
"""
from __future__ import absolute_import
import os
import time

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

# TARGET = 36000000
TARGET = 250

def main():

    # Part 1
    gen = generate_presents_for_house(10)
    presents_dropped = 0
    house = 0
    while presents_dropped < TARGET:
        house, presents_dropped = next(gen)

    print(f"House {house}: {presents_dropped}")

    # Part 2


def generate_presents_for_house(presents_per_house: int):
    house_num = 1

    while True:
        factors = get_factors(house_num)
        print(f"House {house_num}: {factors}")
        yield house_num, sum(map(lambda x: (x * presents_per_house), factors))
        house_num += 1


def get_factors(num: int) -> set[int]:
    factors = set()

    # E.g. factors of 8 = 1, 2, 4, 8
    # iterate from 1 to sqrt of 8, where %=0, i.e. 1 and 2
    # For 1, we add 1 and 8
    # For 2, we add 2 and 4
    # The set eliminates duplicates, e.g. if num is 4, we only want one 2
    for i in range(1, (int(num**0.5) + 1)):
        if num%i == 0:
            factors.add(i)
            factors.add(num//i)
    
    return factors


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
