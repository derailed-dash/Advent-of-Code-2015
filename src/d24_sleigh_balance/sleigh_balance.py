""" 
Author: Darren
Date: 02/05/2021

Solving https://adventofcode.com/2015/day/24


Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import
import logging
import os
import time
from itertools import combinations_with_replacement

# pylint: disable=logging-fstring-interpolation

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"
NUMBER_OF_BAGS = 3


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:\t%(message)s")
    
    input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    # input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        package_weights = [int(x) for x in f.read().splitlines()]

    logging.debug(f"Data: {package_weights}")
    
    # start by getting permutations of sizes for the three bags
    package_count = len(package_weights)
    
    # e.g. from 10 bags, we would get (1, 1, 8), (1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 2, 6), (2, 3, 5), etc
    bags_count_combos = get_bag_size_combos(list(range(1, package_count)), package_count, NUMBER_OF_BAGS)
    for bag_count_combo in bags_count_combos:
        logging.debug(f"Bag count combo: {bag_count_combo}")

        # now determine permutations of packages that give the same weight in each bag.
        # e.g. we want permutations of package weights where (2, 3, 5) packages result in 3 bags that weigh the same
        # we need to recurse now...
            
    
def get_bag_size_combos(package_counts: list[int], total_packages: int, num_bags: int):
    """ Determine combination of terms that add up to the target

    Args:
        entries ([list]): List of int values
        target ([int]): The target sum of any n terms
        num_terms ([int]): The number of terms, n, that must add up to the target

    Returns:
        [type]: [description]
    """
    for num_list in combinations_with_replacement(package_counts, num_bags):
        the_sum = sum(num_list)
        if the_sum == total_packages:
            yield num_list
    

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    