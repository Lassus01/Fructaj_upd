from Card import *
class Deck:
    def __init__(self):
        self.cards = []

    def create(self, fruits, num_cards):
        max_fruits_per_card = 15
        while len(self.cards) < num_cards:
            card_fruits = []
            while len(card_fruits) < max_fruits_per_card:
                random_fruit = random.choice(fruits)
                if card_fruits.count(random_fruit) >= 5:
                    continue
                card_fruits.append(random_fruit)
            if card_fruits in self.cards:
                continue
            self.cards.append(Card(card_fruits))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()