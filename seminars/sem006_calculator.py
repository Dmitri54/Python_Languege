# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension 
# (продолжение)
# ============================================================================================
# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;
# ===============================================================================================
# Сначала ищу знаки с наивысшим приоритетом.
# Калькулируем цифру с двух сторон знака.
# Нахожу знаки с меньшим приоритетом и калькулирую их.
# Вывод результата
# -----------------------------------------------------------------------------------------------
# my_str = '10+200*3'

# my_lst = []
# buf = ''
# for i in range(len(my_str)):
#     if my_str[i].isdigit():
#         buf += my_str[i]
#     else:
#         my_lst.append(int(buf))
#         my_lst.append(my_str[i])
#         buf = ''
# else:
#     my_lst.append(int(buf))
# print(my_lst) # [10, '+', 200, '*', '3'] Список


# while ('*' in my_lst) or ('/' in my_lst):
#     mult = -1
#     if '*' in my_lst:
#         mult = my_lst.index('*')

#     div = -1
#     if '/' in my_lst:
#         div = my_lst.index('/')

#     if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
#         res = my_lst[mult - 1] * my_lst[mult + 1]
#         my_lst = my_lst[:mult - 1] + [res] + my_lst[mult + 2:]

#     elif (div < mult) and (div != -1) and (mult != -1) or ((div != -1) and (mult == -1)):
#         res = my_lst[div - 1] / my_lst[div + 1]
#         my_lst = my_lst[:div - 1] + [res] + my_lst[div + 2:]

# while ('+' in my_lst) or ('-' in my_lst):
#     plus = -1
#     if '+' in my_lst:
#         plus = my_lst.index('+')

#     minus = -1
#     if '-' in my_lst:
#         minus = my_lst.index('-')

#     if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
#         res = my_lst[plus - 1] + my_lst[plus + 1]
#         my_lst = my_lst[:plus - 1] + [res] + my_lst[plus + 2:]

#     elif (minus < plus) and (minus != -1) and (plus != -1) or ((minus != -1) and (plus == -1)):
#         res = my_lst[minus - 1] - my_lst[minus + 1]
#         my_lst = my_lst[:minus - 1] + [res] + my_lst[minus + 2:]

# print(my_lst) # [610]  
# -----------------------------------------------------------------------------------------------
# print(eval('10+200*3')) # Не нужно использовать, т.к. если ввести команды, можно сломать ОП.

