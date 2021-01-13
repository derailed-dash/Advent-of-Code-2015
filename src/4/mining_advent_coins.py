""" 
Author: Darren
Date: 13/01/2021

Solving https://adventofcode.com/2015/day/4

Determine first MD5 hex digest of seed + str representation of a number n,
where the resulting hex digest starts with 5, 6 zeroes.
What is the value of n?
"""
import sys
import os
import time
import hashlib

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"


def main():
    # input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        hash_seed = f.read()
    
    counter = 0
    while True:
        input = hash_seed + str(counter)
        # Create byte equivalent of input string, then generate md5 hexdigest.
        hash_hex = hashlib.md5(input.encode()).hexdigest()
        counter += 1
        if hash_hex.startswith("000000"):
            print(f"With input {input}, hash = {hash_hex}")
            break


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")