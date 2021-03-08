""" 
Author: Darren
Date: 08/03/2021

Solving https://adventofcode.com/2015/day/18

// Overview


Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import
import os
import time

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

def main():
    input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    # input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")