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
from d22_wizards_factories_constants.players_and_wizards import Player, Wizard, SpellFactory


SCRIPT_DIR = os.path.dirname(__file__) 
BOSS_FILE = "input/boss_stats.txt"

def main():
    boss_file = os.path.join(SCRIPT_DIR, BOSS_FILE)
    
    # boss stats are determined by an input file
    with open(boss_file, mode="rt") as f:
        data = f.read().splitlines()
    
    # hit_points, damage = process_boss_input(data)
    # boss = Player("Boss", hit_points=hit_points, damage=damage, armor=0)
    # print(boss)

    # player = Wizard("Bob", hit_points=10, mana=250)
    # print(f"{player}\n")

def play_game(attacks: list, player: Wizard, boss: Player) -> tuple:
    """ Play a game, given a player (Wizard) and an opponent (boss)

    Args:
        attacks (list[str]): List of spells to cast, from SpellFactory.SpellConstants
        player (Wizard): A Wizard
        boss (Player): A mundane opponent

    Returns:
        bool: Whether the player won
    """
    i = 1
    current_player = player
    other_player = boss    

    mana_consumed: int = 0

    while (player.get_hit_points() > 0 and boss.get_hit_points() > 0):
        if current_player == player:
            # player (wizard) attack
            print(f"\nRound {i}...")

            print(f"{current_player.get_name()}'s turn:")
            mana_consumed += player.take_turn(attacks[i-1], boss)
        else:
            i += 1

            print(f"{current_player.get_name()}'s turn:")
            # effects apply before opponent attacks
            player.opponent_takes_turn(boss)
            if boss.get_hit_points() <= 0:
                print(f"Effects killed {boss.get_name()}!")
                continue

            boss.attack(other_player)

        print(f"End of turn: {player}")
        print(f"End of turn: {boss}")

        # swap players
        current_player, other_player = other_player, current_player

    player_won = player.get_hit_points() > 0
    return player_won, mana_consumed


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
