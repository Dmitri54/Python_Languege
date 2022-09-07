# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
number = input('Введите число целое или дробное: ')
def sumNumbers(num):
    sum = 0
    for i in str(num):
        if (i != ",") and (i != "."):
            sum += int(i)
    return sum
print(f"Сумма цифр числа {number} = {sumNumbers(number)}")
