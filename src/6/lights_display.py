""" 
Author: Darren
Date: 14/01/2021

Solving https://adventofcode.com/2015/day/6

Configure 1m lights in a 1000x1000 grid, by following a set of instructions.
Lights begin turned off.
Coords are 0-indexed

Solution 1 of 1:


Part 1:

Part 2:

"""
import sys
import os
import time
import re
import numpy as np

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

def main():
    input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    # input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()

    lights = np.zeros((30,30), dtype=np.int8)
    print(f"Array size: {lights.size}")
    print(lights)


    process_instructions(data, lights)

def process_instructions(data, lights):
    p = re.compile(r"(\d+)\D+(\d+)")

    for line in data:
        line = line.replace(",", "")
        coords = p.search(line).groups()
        coords = list(map(int, coords))

        print(coords)

        if "toggle" in line:
            pass
        elif "on" in line:
            pass
        elif "off" in line:
            pass


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")