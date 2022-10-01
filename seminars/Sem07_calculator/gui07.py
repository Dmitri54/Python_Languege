# Модуль, ввода информации пользователем.

def get_input(): # Функция запрашивает у пользователя два числа и сохраняет в список.
    number_a = input('Enter number: ') # Первая строка
    equation = input('Enter equation: ') # Вторая
    number_b = input('Enter number: ') # Третья
    numbers = number_a + ' ' + equation + ' ' + number_b
    
    return numbers


def send__info(a):
    print(f'Your result: {a}')

