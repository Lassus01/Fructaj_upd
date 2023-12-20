class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def __repr__(self):
        return self.name

    def make_guess(self):
        return input(f"{self.name}, ваше предположение: ")