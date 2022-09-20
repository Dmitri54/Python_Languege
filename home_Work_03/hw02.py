# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from math import ceil

# def mut_elem(list):
#     newList = []
#     for i in range (len(list)//2):
        # lenList = len(list)
        # num = list[i] * list[lenList - i - 1]
        # newList.append(num)
        # if (lenList % 2 != 0):
        #     newnum = list[lenList // 2] ** 2
        #     newList.append(newnum)
#     else:
#         return newList
# lst = [2, 3, 5, 6]
# print(mut_elem(lst)) # [12, 15] - Решение не доделано.

# from math import ceil

# def mut_elem(list):
        
#     if (len(list) % 2 == 0):
#         ten = (len(list) // 2)
#     else:
#         ten = (len(list) // 2) + 1
#     newList = []
#     for i in range (ten):
#         num = list[i] * list[ten - 1 - i]
#         newList.append(num)
#     if (len(list) % 2 != 0):
#         newList[ten - 1] = list[ten - 1]
#     return newList

    
# resultList = [2, 3, 5, 6]
# print(mut_elem(resultList))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def strPrint(strNum):
#     numbers = []
#     for i in range(len(strNum)):
#         numbers.append(float(strNum[i]))
#     return strNum



# outstr = input('Введите строку чисел через пробел: ').split(' ')
# print('Исходный массив: ')
# print(strPrint(outstr)) # ['1.1', '1.2', '3.2', '10.01']



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи
# --------------------------------------------------------------------------------------------------

 
# n = int(input('Введите число и нажмите Enter: '))

# def fibona(num):
#     fib0 = 0
#     fib1 = fib2 = 1
#     print(fib0, fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ') # 0 1 1 2 3 5 8 13 21

# list = fibona(n)

# num = int(input('Введите число и нажмите Enter: '))

# def fib(n):
#    if n in [0]:
#       return 0
#    if n in [1, 2]:
#         return 1
#    else:
#         return fib(n - 1) + fib(n - 2)
# list = []
# for e in range(1, num + 1):
#         list.append(fib(e))
# print(list) # [1, 1, 2, 3, 5]
