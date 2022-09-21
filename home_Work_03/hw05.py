# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи
# -------------------------------------------------------------------------------------------------


def fibonacci(number): # Вычисляет число Фибоначчи
    if number == 0:
        return 0
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def number_fibo(number):
    fibo_list = []
    for i in range(number):
        fibo_list.append(fibonacci(i))
    return fibo_list


def negative_fib(numbers: list):
    new_list = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            new_list.append(numbers[i] * - 1)
        else:
            new_list.append(numbers[i])
    new_list.reverse()
    new_list.remove(0)
    return new_list
        

num = int(input('Введите число и нажмите Enter: '))
array = number_fibo(num)
negative_array = negative_fib(array)
negative_array.extend(array)
print(negative_array) # [34, -21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

