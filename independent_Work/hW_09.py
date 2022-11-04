# 9. Напишу программу, которая выводит случайное число 
# из отрезка [10, 99] и показывает наибольшую цифру числа.
# 78 -> 8
# 12 -> 2
# 85 -> 8
# ===========================================================================================================
import random

rndNum = random.randint(10,100)

print(f'Случайное число из отрезка 10 - 99 => {rndNum}')

firstDigit = rndNum // 10
secondDigit = rndNum % 2

if firstDigit > secondDigit:
    print(f'Наибольшая цифра цисла {rndNum} => {firstDigit}')
else:
    print(f'Наибольшая цифра цисла {rndNum} => {secondDigit}')

