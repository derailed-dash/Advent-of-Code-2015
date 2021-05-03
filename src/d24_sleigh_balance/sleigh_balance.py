""" 
Author: Darren
Date: 02/05/2021

Solving https://adventofcode.com/2015/day/24

We require three bags of equal weight. 
   Bag 1 in the passenger compartment, needs to have fewest packages.
   Bags 2 and 3 to either side.
   
Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import
import logging
import os
import time
from math import prod
from itertools import combinations

# pylint: disable=logging-fstring-interpolation

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:\t%(message)s")
    
    # input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        package_weights = set(int(x) for x in f.read().splitlines())
    
    # Part 1
    distribute_packages(package_weights, 3)
    
    # Part 2
    # distribute_packages(package_weights, 4)


def distribute_packages(package_weights, number_of_bags):
    logging.info(f"Solving for {number_of_bags} bags")
    
    package_count = len(package_weights)
    total_weight = sum(package_weights)
    target_weight_per_bag = total_weight // number_of_bags
    
    logging.debug(f"Package weights: {package_weights}")
    logging.debug(f"Total packages: {package_count}, with total weight: {total_weight}")
    logging.debug(f"Target weight per bag: {target_weight_per_bag}")
    
    first_bag_combos = subset_sum(package_weights, target_weight_per_bag)
    # sort by set size, since the first bag should have fewest packages
    first_bag_combos = sorted(first_bag_combos, key=lambda x: len(x))
    
    shortest_bag_length = package_count
    lowest_quantum_entanglement = get_quantum_entanglement(tuple(package_weights))
    
    for first_bag_combo in first_bag_combos:
        # First bag must have smallest number of packages
        # Skip any bag combos that have more packages than a previous solution
        if len(first_bag_combo) > shortest_bag_length:
            continue
        
        # Skip any solutions with higher QE than existing solutions
        if get_quantum_entanglement(first_bag_combo) >= lowest_quantum_entanglement:
            continue
        
        remaining_package_weights = package_weights - set(first_bag_combo)
        for second_bag_combo in subset_sum(remaining_package_weights, target_weight_per_bag):
            if len(second_bag_combo) < len(first_bag_combo):
                continue
            
            third_bag_combo = tuple(remaining_package_weights - set(second_bag_combo))
            if len(third_bag_combo) < len(second_bag_combo):
                continue
            
            shortest_bag_length = len(first_bag_combo)
            lowest_quantum_entanglement = get_quantum_entanglement(first_bag_combo)
            logging.info(f"Solution found with QE {lowest_quantum_entanglement}")
            logging.info(f"First bag: {first_bag_combo}")
            
            # We don't need any more ways of organising the other bags
            break
            

def get_quantum_entanglement(bag: tuple):
    return prod(bag)


def subset_sum(items, target: int) -> tuple:
    """ Return a tuple of any combinations of items that adds up to the target

    Args:
        items (Sequence): List/set of items
        target (int): The target sum to achieve

    Yields:
        Iterator[tuple]: Items that achieve the desired sum
    """
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    for i in range(len(items)+1):
        for subset in combinations(items, i):
              
            # printing the subset if its sum is x:
            if sum(subset) == target:
                yield subset
                

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    