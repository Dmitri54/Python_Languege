# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
# ===========================================================================================================
number = input('Введите число целое или дробное: ')
sum = 0
for i in str(number):
    if (i != ",") and (i != "."):
        sum += int(i)
print(f"Сумма цифр числа {number} -> {sum}")

