from Deck import *
class FruitageGame:
    def __init__(self, players, fruits):
        self.players = players  # Список игроков
        self.deck = Deck()  # Создаем колоду
        self.deck.create(fruits, 54)
        self.round = 1  # Текущий раунд
        self.current_card = None  # Текущая перевернутая карта
        self.active_player = None  # Текущий активный игрок
        self.winner = None  # Победитель игры

    def start_game(self):
        self.active_player = random.choice(self.players)  # Начинает случайный игрок
        self.play_round()

    def play_round(self):
        print(f"Раунд {self.round}")
        self.current_card = self.deck.draw()  # Переворачиваем верхнюю карту
        print("Текущая карта раунда:", self.current_card)

        if self.current_card.type == "Fruit":
            # Если на карте изображен фрукт, игроки должны назвать количество таких фруктов
            self.play_fruit_round()
        elif self.current_card.type == "Number":
            # Если на карте изображена цифра, игроки должны назвать фрукт, который изображен столько раз
            self.play_number_round()

    def play_fruit_round(self):
        correct_count = self.current_card.count
        print(f"Угадайте количество фрукта {self.current_card.fruit} на карточке!")
        answered_correctly = True
        while answered_correctly:
            guess = self.active_player.make_guess()  # Текущий игрок делает предположение
            if int(guess) == correct_count:
                self.update_scores()
                print(f"Верно! Игрок {self.active_player} получает очко. Текущее количество очков {self.active_player.score}")
                answered_correctly = False
            else:
                print("Неверное предположение")
                print(f"Ход переходит к игроку {self.active_player}")
            self.switch_active_player()
        self.check_end_game()

        if not self.winner:
            self.round += 1
            self.play_round()

    def play_number_round(self):
            correct_fruit = self.current_card.fruit
            print(f"Угадай фрукт c количеством {self.current_card.count} на карточке!")
            answered_correctly = True
            while answered_correctly:
                guess = self.active_player.make_guess()  # Каждый игрок делает предположение
                if guess == correct_fruit:
                    self.update_scores()
                    print(f"Верно! Игрок {self.active_player} получает очко. Текущее количество очков {self.active_player.score}")
                    answered_correctly = False
                else:
                    print("Неверное предположение")
                    self.switch_active_player()
                    print(f"Ход переходит к игроку {self.active_player}")
            self.check_end_game()

            if not self.winner:
                self.round += 1
                self.play_round()

    def switch_active_player(self):
        index = self.players.index(self.active_player)
        index = (index + 1) % len(self.players)  # Переход к следующему игроку
        self.active_player = self.players[index]

    def update_scores(self):
        self.active_player.score += 1  # Активный игрок получает победное очко

    def check_end_game(self):
        if len(self.deck.cards) == 2:
            # Когда на столе остается 2 карты, игра завершается
            self.calculate_winner()

    def calculate_winner(self):
        max_score = max(player.score for player in self.players)
        winners = [player for player in self.players if player.score == max_score]
        if len(winners) == 1:
            self.winner = winners[0]
        else:
            self.winner = None  # Ничья

        print("Игра окончена!")
        if self.winner:
            print("Победитель:", self.winner)
        else:
            print("Ничья!")