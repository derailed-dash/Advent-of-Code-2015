""" 
Author: Darren
Date: 13/03/2021

Solving https://adventofcode.com/2015/day/19

Start with input molecule and then replace components, one per step, 
until it has the right molecule.

E.g. input of:
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO

Part 1:
    Calibration: how many molecules can be generated in one step?

    Read input and build defaultdict of source groups to target groups (1 to many).
    At the same time, let's build a dict of target groups to src groups (1 to 1).

    For each src group:
        Match each position in the medicine molecule.
        For each match, and for each target group, 
            concatenate prefix + target group + suffix.

Part 2:
    Number of iterations to go from e to target molecule.

    This time, go through all target groups.
"""
from __future__ import absolute_import
import os
import time
import re
from collections import defaultdict
from typing import Tuple

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

def main():
    input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    # input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()

    src_groups, target_groups, medicine_molecule = process_input(data)

    new_molecules = substitute_groups(src_groups, medicine_molecule)

    unique_new_molecules = set(new_molecules)
    print(unique_new_molecules)
    print(f"Part 1: Identified {len(unique_new_molecules)} unique molecules")


def substitute_groups(groups, medicine_molecule) -> list:
    new_molecules = []

    # go through all the groups we have substitutions for
    for group, targets in groups.items():
        # get all matching positions for this group
        group_matches = re.finditer(group, medicine_molecule)

        # move left to right, matching group one at a time
        for group_match in group_matches:
            start, end = group_match.span()
            prefix = medicine_molecule[:start]
            suffix = medicine_molecule[end:]

            # replace the current group occurrence with each target
            for target in targets:
                new_molecules.append(prefix + target + suffix)
    
    return new_molecules


def process_input(data: list) -> Tuple[dict, dict, str]:
    subst_match = re.compile(r"^(\w+) => (\w+)")
    
    # each src group can make many target groups
    src_groups = defaultdict(list)

    # each target group can be made from only one src group
    target_groups = {}

    for line in data:
        if "=>" in line:
            group, target_group = subst_match.match(line).groups()
            src_groups[group] += [target_group]
            target_groups[target_group] = group

    return src_groups, target_groups, data[-1]


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
