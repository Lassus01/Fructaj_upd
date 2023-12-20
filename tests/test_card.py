from Card import Card

def test_card_initialization():
    fruits = ["apple", "banana", "orange"]
    card = Card(fruits)
    assert card.front == fruits
    assert card.back == 1 or card.back in fruits  # Случайное число
    assert card.type in ["Fruit", "Number"]
    assert card.fruit in fruits
    assert card.count == fruits.count(card.fruit)

def test_card_representation():
    fruits = ["apple", "banana", "orange"]
    card = Card(fruits)
    assert repr(card) == f"Лицевая сторона: {' '.join(fruits)}, Задняя сторона: {card.back}, Тип: {card.type}"