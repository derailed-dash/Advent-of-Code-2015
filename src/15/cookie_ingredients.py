""" 
Author: Darren
Date: 16/02/2021

Solving https://adventofcode.com/2015/day/15

// Overview


Solution:

Part 1:

Part 2:

"""
import sys
import os
import time
from itertools import permutations
from math import prod as prod
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"


class Ingredient:
    CALORIES = "calories"

    def __init__(self, name: str, properties: dict) -> None:
        self._name = name
        self._properties = properties
        self._calories = self._properties.pop(Ingredient.CALORIES)

    def get_properties(self) -> dict:
        return self._properties

    def get_calories(self) -> int:
        return self._calories

    def __str__(self) -> str:
        return self._name

    def __repr__(self):
        return (f"{self.__class__.__name__}: {self._name}")


def main():
    # input_file = os.path.join(SCRIPT_DIR, SAMPLE_INPUT_FILE)
    input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()

    ingr_list = process_ingredients(data)

    cookies = {}
    combos = find_combos(100, len(ingr_list))
    for combo in combos:
        # e.g. with 2 ingredients, a combo might be [44, 56]
        prop_scores = defaultdict(int)
        for i, qty in enumerate(combo):
            ingr: Ingredient
            ingr = ingr_list[i]
            for prop, value in ingr.get_properties().items():
                prop_scores[prop] += qty * value

        for prop, value in prop_scores.items():
            if value < 0:
                prop_scores[prop] = 0
    
        total_score = prod(prop_scores.values())
        cookies[combo] = total_score
    
    best_cookie = max(cookies.items(), key=lambda x: x[1])
    print(f"Best cookie {best_cookie[0]} with score: {best_cookie[1]}")


def find_combos(target: int, terms: int) -> list: 
    """Return all combinations of terms that sum to the target numberself.
    E.g. if target = 5 and terms = 2, the results would be:
    (0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)

    Args:
        target (int): The sum our terms need to add up to
        terms (int): How many terms need to add up to the sum

    Returns:
        list: Tuples of valid term combinations
    """
    return [combo for combo in permutations(range(target), terms) if sum(combo) == target] 


def process_ingredients(data: list):
    ingr_list = []

    line: str
    for line in data:
        name, properties = line.split(":")
        properties = [x.strip().split(" ") for x in properties.split(",")]
        props_dict = {prop[0]:int(prop[1]) for prop in properties}
        ingr_list.append(Ingredient(name, props_dict))

    return ingr_list


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")