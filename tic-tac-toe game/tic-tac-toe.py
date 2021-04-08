class GameXO:

    def __init__(self):
        self.field = "|0|1|2|\n|3|4|5|\n|6|7|8|"
        self.winning_combinations = [(1, 3, 5), (9, 11, 13), (17, 19, 21),
                                     (1, 9, 17), (3, 11, 19), (5, 13, 21),
                                     (1, 11, 21), (5, 11, 17)
                                     ]

    def game(self):
        turn = 1
        while True:
            if turn % 2 != 0:
                x_or_o = "X"
            else:
                x_or_o = "O"
            your_step = int(input('Введите индекс поля: '))
            new_field = self.field.replace(f'{self.get_key(your_step)}', f'{x_or_o}')
            self.field = new_field
            turn += 1
            print(self.field)
            if self.game_wins():
                return f'{self.game_wins()} wins'
            else:
                continue

    def game_wins(self):
        for (x, y, z) in self.winning_combinations:
            if self.field[x] == self.field[y] and self.field[z] == self.field[y] and (self.field[x] == 'X' or 'O'):
                return self.field[x]

    def field(self):
        return self.field

    def game_dict(self):
        field_dict = {
            self.field[1]: 0, self.field[3]: 1, self.field[5]: 2,
            self.field[9]: 3, self.field[11]: 4, self.field[13]: 5,
            self.field[17]: 6, self.field[19]: 7, self.field[21]: 8
        }
        return field_dict

    def get_key(self, value):
        field_dict = self.game_dict()
        for k, v in field_dict.items():
            if v == value:
                return k


print(GameXO().field)
print(GameXO().game())
