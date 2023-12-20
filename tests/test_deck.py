from Deck import Deck

def test_deck_creation():
    deck = Deck()
    fruits = ["apple", "banana", "orange"]
    num_cards = 10
    deck.create(fruits, num_cards)
    assert len(deck.cards) == num_cards

def test_deck_draw():
    deck = Deck()
    fruits = ["apple", "banana", "orange"]
    num_cards = 10
    deck.create(fruits, num_cards)
    card = deck.draw()
    assert card not in deck.cards
    assert len(deck.cards) == num_cards - 1