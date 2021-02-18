""" 
Author: Darren
Date: 16/02/2021

Solving https://adventofcode.com/2015/day/15

Cookie recipes contain exactly 100 spoonfulls of ingredients.
Each ingredient is made up of 5 properties: capacity, durability, flavour, texture, calories.
Each ingredient has a score for each of these properties.
Score of each property = qty1 * ingr1 + qt2 * ingr2... (or 0 if score is -ve)

Overall cookie score = product of all properties

Solution:

Part 1:
    Get all permutations of quantities that sum to 100, 
    where the number of quantities is the number of ingredients.
    For each combo of ingredients, compute sum of quantities * prop.
    Cookie class to store combo, score, and calories.
    Determine score of best cookie.    

Part 2:
    Filter cookies list where calories == 500.
    Repeat approach to get cookie with highest score, from this new subset.
"""
import sys
import os
import time
from itertools import permutations
from math import prod
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"
SAMPLE_INPUT_FILE = "input/sample_input.txt"

CAL_TARGET = 500
INGREDIENT_QTY = 100


class Cookie:
    def __init__(self, combo: tuple, score: int, calories:int) -> None:
        self._combo = combo
        self._score = score
        self._calories = calories

    def get_combo(self):
        return self._combo
    
    def get_calories(self) -> int:
        return self._calories

    def get_score(self) -> int:
        return self._score

    def __str__(self) -> str:
        return f"{str(self._combo)}, cals={self.get_calories()}, score={self.get_score()}"

    def __repr__(self):
        return (f"{self.__class__.__name__}: {self.__str__()}")


class Ingredient:
    CALORIES = "calories"

    def __init__(self, name: str, properties: dict) -> None:
        """Input name and props.

        Args:
            name (str): name of this ingredient
            properties (dict): k:v pairs of all props for this ingredient
                Note that we pop 'calories' and store as a separate property
        """
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

    cookies = []
    combos = find_combos(INGREDIENT_QTY, len(ingr_list))
    for combo in combos:
        # e.g. with 2 ingredients, a combo might be [44, 56]
        prop_scores = defaultdict(int)
        calories = 0
        ingr: Ingredient
        for qty, ingr in zip(combo, ingr_list):
            for prop, value in ingr.get_properties().items():
                prop_scores[prop] += qty * value

            calories += qty * ingr.get_calories()

        for prop, value in prop_scores.items():
            if value < 0:
                prop_scores[prop] = 0
    
        total_score = prod(prop_scores.values())
        cookies.append(Cookie(combo, total_score, calories))
    
    # Let's reduce our cookies down to only those with positive scores
    print(f"A total of {len(cookies)} cookie recipes.")
    cookies = [cookie for cookie in cookies if cookie.get_score() > 0]
    print(f"{len(cookies)} with a positive score.")
    best_cookie = max(cookies, key=get_cookie_score)
    print(f"Best cookie: {best_cookie}")

    # Part 2
    fixed_cal_cookies = [cookie for cookie in cookies if cookie.get_calories() == CAL_TARGET]
    print(f"{len(fixed_cal_cookies)} positive scoring cookies at {CAL_TARGET} calories.")
    best_fixed_cal_cookie = max(fixed_cal_cookies, key=get_cookie_score)
    print(f"Best {CAL_TARGET} calorie cookie: {best_fixed_cal_cookie}")


def get_cookie_score(cookie: Cookie) -> int:
    return cookie.get_score()


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