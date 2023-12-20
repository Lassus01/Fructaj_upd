import pytest
from Player import *

from Player import Player

def test_player_initialization():
    player = Player("John")
    assert player.name == "John"
    assert player.score == 0

def test_player_representation():
    player = Player("John")
    assert repr(player) == "John"