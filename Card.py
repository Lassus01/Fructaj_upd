import random

class Card:
    def __init__(self, fruits):
        self.front = fruits  # Список фруктов на лицевой стороне карты
        self.type = random.choice(["Fruit", "Number"])  # Случайный тип карты
        self.back = None  # Обратная сторона карты
        self.fruit = random.choice(fruits)
        self.count = fruits.count(self.fruit)
        if self.type == "Fruit":
            self.back = self.fruit
        elif self.type == "Number":
            self.back = self.count

    def __repr__(self):
        return f"Лицевая сторона: {' '.join(self.front)}, Задняя сторона: {self.back}, Тип: {self.type}"