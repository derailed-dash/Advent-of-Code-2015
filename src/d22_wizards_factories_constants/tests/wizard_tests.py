""" Test cases for Spell Casting """
from d22_wizards_factories_constants.players_and_wizards import Player, Wizard, SpellFactory
from d22_wizards_factories_constants.spell_casting import play_game as pg

def do_tests():
    # run some tests
    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.POISON, 
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]
    do_test_game("TEST: TEST GAME", test_attacks)

    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.POISON, 
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]    
    do_test_game("TEST: NOT ENOUGH MANA", test_attacks)

    test_attacks = [
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.DRAIN,
        SpellFactory.SpellConstants.SHIELD,
        SpellFactory.SpellConstants.RECHARGE,
        SpellFactory.SpellConstants.MAGIC_MISSILES,
    ]    
    do_test_game("nTEST: SPELL ALREADY ACTIVE", test_attacks)


def do_test_game(game_label: str, attacks: list[str]):
    print(f"\n*** {game_label} ***")
    
    player = Wizard("Bob", hit_points=10, mana=250)
    print(f"{player}")
    boss = Player("Boss Socks", hit_points=14, damage=8, armor=0)
    print(boss)
  
    try:
        player_won, mana_consumed = pg(attacks, player, boss)
        print(f"\nPlayer won? {player_won}. Mana consumed: {mana_consumed}")  
    except ValueError as err:
        print(err)


do_tests()