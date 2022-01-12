import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 1, 2)

def test_single_numbers():
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 2 == Yatzy.ones(1, 1, 3, 4, 5)
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
    assert 0 == Yatzy.threes(1, 1, 1, 4, 5)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)
    # A partir de aquí dejan de ser metodos estaticos.
    # En vez de crear un objeto fuera, he pasado los parametros que quiero testear directamente a la clase
    assert 0 == Yatzy(1, 2, 1, 1, 3).fours()
    assert 4 == Yatzy(1, 2, 3, 4, 5).fours()
    assert 0 == Yatzy(1, 2, 1, 1, 3).fives()
    assert 20 == Yatzy(5, 5, 5, 5, 3).fives()
    assert 0 == Yatzy(1, 2, 1, 1, 3).sixes()
    assert 12 == Yatzy(6, 2, 1, 1, 6).sixes()

def test_pairs():
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(3, 2, 5, 4, 1)

def test_two_pairs():
    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)

def test_three():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 2, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)

def test_poker():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)    
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)    

def test_straights():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)

