""" 
Author: Darren
Date: 19/03/2021

Solving https://adventofcode.com/2015/day/20

Infinite elves deliver to infinite houses numbered sequentially.
Each elf is assigned a number and a progression.
Elfx visits all houses xn. E.g.
    elf1 visits 1, 2, 3, 4 ...
    elf2 visits 2, 4, 6, 8 ...
    elfx visits x, 2x, 3x, 4x ...

At each house, the elf delivers 10x presents.


Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import
import os
import time
import re

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

def main():
    # input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")