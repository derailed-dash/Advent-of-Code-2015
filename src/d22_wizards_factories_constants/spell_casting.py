""" 
Author: Darren
Date: 09/04/2021

Solving https://adventofcode.com/2015/day/22

// Overview


Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import
import os
import time
from d22_wizards_factories_constants.player import Player, Wizard, SpellFactory


SCRIPT_DIR = os.path.dirname(__file__) 
BOSS_FILE = "input/boss_stats.txt"

def main():
    boss_file = os.path.join(SCRIPT_DIR, BOSS_FILE)
    
    # boss stats are determined by an input file
    with open(boss_file, mode="rt") as f:
        data = f.read().splitlines()
    
    hit_points, damage = process_boss_input(data)
    # boss = Player("Boss", hit_points=hit_points, damage=damage, armor=0)
    boss = Player("Boss Socks", hit_points=10, damage=8, armor=0)
    print(boss)

    player = Wizard("Bob", hit_points=10, damage=0, armor=0, mana=250)
    print(f"{player}\n")
    player.cast_spell(SpellFactory.SpellConstants.MAGIC_MISSILES, boss)

    # If we want to play a game and see each attack...  
    player_wins = play_game(player, boss)
    if player_wins:
        print("\nPlayer won!")
    else:
        print("\nBoss won. :(")


def play_game(player: Player, boss: Player) -> bool:
    """Performs a game, given two players. Determines if player1 wins, vs bloss.

    Args:
        player (Player): The player
        boss (Player): The boss

    Returns:
        bool: Whether player wins
    """
    print("*** The Game Begins ***")
    i = 1
    current_player = player
    other_player = boss
    while (player.get_hit_points() > 0 and boss.get_hit_points() > 0):
        if current_player == player:
            print(f"Round {i}...")
        else:
            i += 1

        current_player.attack(other_player)
        print(f"Result = {other_player}")


        current_player, other_player = other_player, current_player
    
    return player.is_alive()


def process_boss_input(data:list[str]) -> tuple:
    """ Process boss file input and return tuple of hit_points, damage and armor

    Args:
        data (List[str]): input file lines

    Returns:
        tuple: hit_points, damage, armor
    """
    boss = {}
    for line in data:
        key, val = line.strip().split(":")
        boss[key] = int(val)

    return boss['Hit Points'], boss['Damage']


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
