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

# pylint: disable=multiple-statements

SCRIPT_DIR = os.path.dirname(__file__) 
BOSS_FILE = "input/boss_stats.txt"

LOGGING_ENABLED = False

# pylint
def main():
    boss_file = os.path.join(SCRIPT_DIR, BOSS_FILE)
    
    # boss stats are determined by an input file
    with open(boss_file, mode="rt") as f:
        data = f.read().splitlines()
    
    boss_hit_points, boss_damage = process_boss_input(data)

    spell_key_lookup = {
        0: SpellFactory.SpellConstants.MAGIC_MISSILES,
        1: SpellFactory.SpellConstants.DRAIN,
        2: SpellFactory.SpellConstants.SHIELD,
        3: SpellFactory.SpellConstants.POISON,
        4: SpellFactory.SpellConstants.RECHARGE
    }

    attack_combos_lookups = attack_combos_generator(9, spell_key_lookup)
    count_combos = len(attack_combos_lookups)

    winning_games = {}
    least_winning_mana = 10000
    while attack_combos_lookups:
        boss = Player("Boss", hit_points=30, damage=boss_damage, armor=0)
        player = Wizard("Bob", hit_points=50, mana=350)
    
        print(f"\nRemaining attack combos: {len(attack_combos_lookups)}")
        print(f"Mana target: {least_winning_mana}")
        attack_combo_lookup = attack_combos_lookups.pop()
        print(f"Current attack: {attack_combo_lookup}")
        # Convert the attack combo to a list of attacks.
        attack_combo = [spell_key_lookup[int(key)] for key in attack_combo_lookup]

        player_won, mana_consumed, rounds_started = play_game(attack_combo, player, boss, mana_target=least_winning_mana)
        if player_won:
            winning_games[mana_consumed] = attack_combo_lookup
            least_winning_mana = min(mana_consumed, least_winning_mana)
        else:
            # For losing games, remove all attack_combos with the same starting attacks. 
            # (To remove combos aborted by exceptions.)
            bad_combo = attack_combo_lookup[0:rounds_started]
            bad_combos = set(filter(lambda l: l[0:rounds_started] == bad_combo, attack_combos_lookups))
            print(f"Eliminating {len(bad_combos)} bad combos starting with {bad_combo}.")
            
            # remove bad_combos attack_combos_lookups
            attack_combos_lookups.difference_update(bad_combos)                        

    print(f"We won {len(winning_games)} out of {count_combos}.")

def to_base_n(number: int, base: int):
    """ Convert any integer number into a base-n string representation of that number.
    E.g. to_base_n(38, 5) = 123

    Args:
        number (int): The number to convert
        base (int): The base to apply

    Returns:
        [str]: The string representation of the number
    """
    ret_str = ""
    while number:
        ret_str = str(number % base) + ret_str
        number //= base

    return ret_str


def attack_combos_generator(max_attacks: int, spell_key_lookup: dict):
    attack_indeces = len(spell_key_lookup)
    num_attack_combos = (attack_indeces**max_attacks)
    
    # use a set so that we can pop as we go, and use some set algebra to remove attacks we know won't work
    attack_combos_lookups = set()

    # build up a list of attack_combos. E.g.
    # [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 1, 0], [0, 1, 1], [0, 1, 2], etc
    for i in range(num_attack_combos):
        # convert i to base-n (where n is the number of attacks we can choose from), 
        # and then pad with zeroes until we have max number of attacks
        attack_combos_lookups.add(to_base_n(i, attack_indeces).zfill(max_attacks))

    return attack_combos_lookups


def play_game(attacks: list, player: Wizard, boss: Player, **kwargs) -> tuple[bool, int, int]:
    """ Play a game, given a player (Wizard) and an opponent (boss)

    Args:
        attacks (list[str]): List of spells to cast, from SpellFactory.SpellConstants
        player (Wizard): A Wizard
        boss (Player): A mundane opponent

    Returns:
        tuple[bool, int, int]: Whether the player won, the amount of mana consumed, and the number of rounds started
    """
    i = 1
    current_player = player
    other_player = boss    

    mana_consumed: int = 0
    mana_target = kwargs.get('mana_target', None)

    while (player.get_hit_points() > 0 and boss.get_hit_points() > 0):
        if current_player == player:
            # player (wizard) attack
            if LOGGING_ENABLED: print(f"\nRound {i}...")

            if LOGGING_ENABLED: print(f"{current_player.get_name()}'s turn:")
            try:
                mana_consumed += player.take_turn(attacks[i-1], boss)
                if mana_target and mana_consumed > mana_target:
                    raise ValueError(f'Mana target {mana_target} exceeded; mana consumed={mana_consumed}.')
            except ValueError as err:
                print(err)
                return False, mana_consumed, i

        else:
            if LOGGING_ENABLED: print(f"{current_player.get_name()}'s turn:")
            # effects apply before opponent attacks
            player.opponent_takes_turn(boss)
            if boss.get_hit_points() <= 0:
                if LOGGING_ENABLED: print(f"Effects killed {boss.get_name()}!")
                continue

            boss.attack(other_player)
            i += 1

        if LOGGING_ENABLED: print(f"End of turn: {player}")
        if LOGGING_ENABLED: print(f"End of turn: {boss}")

        # swap players
        current_player, other_player = other_player, current_player

    player_won = player.get_hit_points() > 0
    return player_won, mana_consumed, i


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
