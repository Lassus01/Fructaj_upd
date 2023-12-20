from Game import FruitageGame
from Player import Player

def test_game_initialization():
    player1 = Player("John")
    player2 = Player("Alice")
    fruits = ["apple", "banana", "orange"]
    game = FruitageGame([player1, player2], fruits)
    assert len(game.players) == 2
    assert game.deck is not None
    assert game.round == 1
    assert game.current_card is None
    assert game.active_player is None
    assert game.winner is None