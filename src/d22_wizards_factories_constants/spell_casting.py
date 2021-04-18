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

    # run some tests
    # test_game()
    test_not_enough_mana()
    test_spell_already_active()

def test_game():
    print("\nTEST GAME")
    
    player = Wizard("Bob", hit_points=10, mana=250)
    print(f"{player}")
    boss = Player("Boss Socks", hit_points=14, damage=8, armor=0)
    print(boss)
    
    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.POISON, 
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]
    
    try:
        play_game(test_attacks, player, boss)
    except ValueError as err:
        print(err)   

def test_not_enough_mana():
    print("\nTEST NOT ENOUGH MANA")   

    player = Wizard("Bob", hit_points=10, mana=250)
    print(f"{player}")
    boss = Player("Boss Socks", hit_points=14, damage=8, armor=0)
    print(boss)
 
    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.POISON, 
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]
    try:
        play_game(test_attacks, player, boss)
    except ValueError as err:
        print(err)    

def test_spell_already_active():
    print("\nTEST SPELL ALREADY ACTIVE")

    player = Wizard("Bob", hit_points=10, mana=250)
    print(f"{player}")
    boss = Player("Boss Socks", hit_points=14, damage=8, armor=0)
    print(boss)

    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]
    try:
        play_game(test_attacks, player, boss)
    except ValueError as err:
        print(err)   

def play_game(attacks: list, player: Wizard, boss: Player):
    i = 1
    current_player = player
    other_player = boss    

    while (player.get_hit_points() > 0 and boss.get_hit_points() > 0):
        if current_player == player:
            # player (wizard) attack
            print(f"\nRound {i}...")

            print(f"{current_player.get_name()}'s turn:")
            player.take_turn(attacks[i-1], boss)
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

    if player.get_hit_points() > 0:
        print("Player won!")
    else:
        print("Boss won. :(")


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
