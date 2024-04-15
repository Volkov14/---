from random import randint

class Game_3x3:
    def __init__(self):
        self.field = [["." for _ in range(3)] for _ in range(3)]

    def user_round(self):
        print("Выберите столбец и строку для хода")
        self.horizontal = int(input("Введите столбец:")) - 1
        self.vertical = int(input("Введите строку:")) - 1
        if self.field[self.vertical][self.horizontal] == ".":
            self.field[self.vertical][self.horizontal] = "X"
        else:
            print("Эта клетка уже занята, выберите другую клетку")
            self.user_round()
        self.draw_field()
        if self.check_winner("X"):
            print("Вы выиграли!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.pc_round()

    def pc_round(self):
        while True:
            self.horizontal = randint(0, 2)
            self.vertical = randint(0, 2)
            if self.field[self.vertical][self.horizontal] == ".":
                self.field[self.vertical][self.horizontal] = "O"
                break
        self.draw_field()
        if self.check_winner("O"):
            print("Выиграл компьютер!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.user_round()

    def draw_field(self):
        for row in self.field:
            print(" ".join(row))
        print("\n")

    def check_winner(self, full):
        # Проверка строк
        for row in self.field:
            if all(cell == full for cell in row):
                return True

        # Проверка столбцов
        for col in range(3):
            if all(self.field[row][col] == full for row in range(3)):
                return True

        # Проверка диагоналей
        if all(self.field[i][i] == full for i in range(3)) or all(self.field[i][2 - i] == full for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(cell != "." for row in self.field for cell in row)


class Game_4x4:
    def __init__(self):
        self.field = [["." for _ in range(4)] for _ in range(4)]

    def user_round(self):
        print("Выберите столбец и строку для хода")
        self.horizontal = int(input("Введите столбец:")) - 1
        self.vertical = int(input("Введите строку:")) - 1
        if self.field[self.vertical][self.horizontal] == ".":
            self.field[self.vertical][self.horizontal] = "X"
        else:
            print("Эта клетка уже занята, выберите другую клетку")
            self.user_round()
        self.draw_field()
        if self.check_winner("X"):
            print("Вы выиграли!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.pc_round()

    def pc_round(self):
        while True:
            self.horizontal = randint(0, 3)
            self.vertical = randint(0, 3)
            if self.field[self.vertical][self.horizontal] == ".":
                self.field[self.vertical][self.horizontal] = "O"
                break
        self.draw_field()
        if self.check_winner("O"):
            print("Выиграл компьютер!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.user_round()

    def draw_field(self):
        for row in self.field:
            print(" ".join(row))
        print("\n")

    def check_winner(self, full):
        # Проверка строк
        for row in self.field:
            if all(cell == full for cell in row):
                return True

        # Проверка столбцов
        for col in range(4):
            if all(self.field[row][col] == full for row in range(4)):
                return True

        # Проверка диагоналей
        if all(self.field[i][i] == full for i in range(4)) or all(self.field[i][3 - i] == full for i in range(4)):
            return True

        return False

    def check_draw(self):
        return all(cell != "." for row in self.field for cell in row)


class Game_5x5:
    def __init__(self):
        self.field = [["." for _ in range(5)] for _ in range(5)]

    def user_round(self):
        print("Выберите столбец и строку для хода")
        self.horizontal = int(input("Введите столбец:")) - 1
        self.vertical = int(input("Введите строку:")) - 1
        if self.field[self.vertical][self.horizontal] == ".":
            self.field[self.vertical][self.horizontal] = "X"
        else:
            print("Эта клетка уже занята, выберите другую клетку")
            self.user_round()
        self.draw_field()
        if self.check_winner("X"):
            print("Вы выиграли!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.pc_round()

    def pc_round(self):
        while True:
            self.horizontal = randint(0, 4)
            self.vertical = randint(0, 4)
            if self.field[self.vertical][self.horizontal] == ".":
                self.field[self.vertical][self.horizontal] = "O"
                break
        self.draw_field()
        if self.check_winner("O"):
            print("Выиграл компьютер!")
            return
        if self.check_draw():
            print("Ничья!")
            return
        self.user_round()

    def draw_field(self):
        for row in self.field:
            print(" ".join(row))
        print("\n")

    def check_winner(self, full):
        # Проверка строк
        for row in self.field:
            if all(cell == full for cell in row):
                return True

        # Проверка столбцов
        for col in range(5):
            if all(self.field[row][col] == full for row in range(5)):
                return True

        # Проверка диагоналей
        if all(self.field[i][i] == full for i in range(5)) or all(self.field[i][4 - i] == full for i in range(5)):
            return True

        return False

    def check_draw(self):
        return all(cell != "." for row in self.field for cell in row)

print ("Выбирите игру:\n1 - поле 3 на 3\n2 - поле 4 на 4\n3 - поле 5 на 5")
choice_game = int(input())
def options_of_game(choice_game):
    if choice_game == 1:
        return Game_3x3()
    elif choice_game == 2:
        return Game_4x4()
    elif choice_game == 3:
        return Game_5x5()

game = options_of_game(choice_game)
game.draw_field()
game.user_round()