# Задача 3. Создайте программу для игры в "Крестики-нолики".
# ------------------------------------------------------------------------------------------------

def draw_board(board): # Функция рисует матрицу с заполненными элементами списка (board).
    print("-" * 13) # Верхняя граница поля
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|") # Разделение столбцов.
        print("-" * 13) # Выведет тринадцать минусов, для разделения строк.


def take_input(player_token): # Функция принимает число от пользователя и проверяет её.
    valid = False
    while not valid:
        player_answer = input("Куда поставим: " + player_token + "? ") # Куда поставить X или 0.

        try:
            player_answer = int(player_answer) # Проверяет ввел ли пользователь число.
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9: # Проверка, введино ли число от 1 до 9.
            if(str(board[player_answer - 1]) not in "XO"): # Проверка, введино X либо O
                board[player_answer - 1] = player_token # Запоминает значение
                valid = True
            else:
                print("Эта клетка уже занята!") # Если она уже занята.
        else:
            print("Введите число от 1 до 9")

def check_win(board): # Функция проверки игрового поля, проверяет выиграл ли игрок.
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # Кортеж с выигрышными вариантами.
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board): # В этой функции собираю воедино программу.
    counter = 0 # Счечик очков
    win = False 
    while not win:
        draw_board(board) # Определяю токен игрока.
        if counter % 2 == 0: # Первый игрок всегда будет X.
            take_input("X")
        else:
            take_input("O")
        counter += 1

        if counter > 4: # Чтобы не было лишнего вызова функции check_win
            tmp = check_win(board) # Присвоил значение вызова функции переменной tmp, чтобы короче писать.
            if tmp:
                print(tmp, "Ты выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


print("*" * 10, "Крестики-нолики v.1.0", "*" * 10) # Для красивого приветствия.
board = list(range(1, 10)) # Создаю список от 1 до 9.

main(board)

# ********** Крестики-нолики v.1.0 **********
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------

# X Ты выиграл!
# -------------
# | X | 2 | O |
# -------------
# | X | X | X |
# -------------
# | 7 | O | O |
# -------------