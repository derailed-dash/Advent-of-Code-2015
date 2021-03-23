""" 
Author: Darren
Date: 23/03/2021

Solving https://adventofcode.com/2015/day/21

Alternating turns for player vs boss.
Loser is first for hit points to reach 0.
Hit points lost = attacker damange - defender armor
(A minimum of 1 hit point lost in any attack.)

Solution:

Part 1:

Part 2:

"""
from __future__ import absolute_import, annotations
import os
import time
import re
from math import ceil

SCRIPT_DIR = os.path.dirname(__file__) 
INPUT_FILE = "input/input.txt"

class Player:
    def __init__(self, name: str, hit_points: int, damage: int, armor: int):
        self._name = name
        self._hit_points = hit_points
        self._damage = damage
        self._armor = armor

    def get_name(self) -> str:
        return self._name

    def get_hit_points(self) -> int:
        return self._hit_points

    def get_armor(self) -> int:
        return self._armor

    def take_hit(self, loss: int):
        self._hit_points -= loss

    def is_alive(self) -> bool:
        return self._hit_points > 0

    def get_attack_damage(self, other_player: Player) -> int:
        """Damage inflicted in an attack.  Given by this player's damage minus other player's armor.

        Args:
            other_player (Player): The defender

        Returns:
            int: The damage inflicted per attack
        """
        return max(self._damage - other_player.get_armor(), 1)

    def get_attacks_needed(self, other_player: Player) -> int:
        """The number of attacks needed for this player to defeat the other player.

        Args:
            other_player (Player): The other player

        Returns:
            int: The number of rounds needed.
        """
        return ceil(other_player.get_hit_points() / self.get_attack_damage(other_player))

    def will_defeat(self, other_player: Player) -> bool:
        return self.get_attacks_needed(other_player) <= other_player.get_attacks_needed(self)

    def attack(self, other_player: Player):
        attack_damage = self.get_attack_damage(other_player)
        other_player.take_hit(attack_damage)
    
    def __str__(self):
        return f"Player: {self._name}, hit points: {self._hit_points}"


def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_FILE)
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()

    player = Player("Player", hit_points=8, damage=5, armor=5)
    boss = Player("Boss", hit_points=12, damage=7, armor=2)

    print(player)
    print(boss)
    print(f"Player attack damage = {player.get_attack_damage(boss)}")
    print(f"Boss attack damage = {boss.get_attack_damage(player)}")

    print(f"\nPlayer attacks needed = {player.get_attacks_needed(boss)}")
    print(f"Boss attacks needed = {boss.get_attacks_needed(player)}")

    print(f"Player wins? {player.will_defeat(boss)}\n")

    player_wins = play_game(player, boss)
    if player_wins:
        print("We won!")
    else:
        print("We lost")

def play_game(player: Player, boss: Player) -> bool:
    print("Playing...")
    i = 1
    current_player = player
    other_player = boss
    while (player.get_hit_points() > 0 and boss.get_hit_points() > 0):
        current_player.attack(other_player)
        print(f"{current_player.get_name()} round {i}")
        print(other_player)
        if current_player == boss:
            i += 1

        current_player, other_player = other_player, current_player
    
    return player.is_alive()

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")