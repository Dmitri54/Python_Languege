# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension 
# (продолжение)
# ---------------------------------------------------------------------------------------------

# a = ['412', '123', '421'] # Есть список в котором лежат строки в виде чисел. 
# Как их быстро превратить в целые числа?
# a = list(map(int, a))
# А если через list Comprehension
# a = [int(item) for item in a if item.isdigit()] # Чтобы получить список чисел.
# Я буду брать из a элемент превращать его в int, превращать в результат, только при условии, если он цифра.
# Если я хочу оставить строки, можно сделать через фильтр и использовать тернарный оператор.

# a = ['412', '*', '123', '+', '421']
# a = list(map(lambda x: int(x) if x.isdigit() else x, a))
# print(a) # [412, '*', 123, '+', 421]

# ----------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------
# list comprehension --------------------------------------------------------------------------------
# Он состоит из трех частей
# что сделать с элементок/ с каким элементом/ при каком условии
# input_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = [item for item in input_list if input_list.count(item) == 1] # input_list.count(item) - сколько раз входит этот элемент 
# print(input_list) # [1, 2, 3, 5, 1, 5, 3, 10]
# print(res) # [2, 10]
# filter --------------------------------------------------------------------------------------------
# res = list(filter(lambda x: x > 2, input_list))
# print(res) # [3, 5, 5, 3, 10]
# res2 = tuple(filter(lambda x: x > 2, input_list))
# print(res2) # кортеж (3, 5, 5, 3, 10)
# res3 = tuple(filter(lambda x: input_list.count(x) == 1, input_list))
# print(res3) # кортеж (2, 10)

# input_list2 = ['423', 'tr', '57', 'aavxc']
# res4 = list(map(lambda x: int(x) if x.isdigit() else x, input_list2))
# print(res4) # [423, 'tr', 57, 'aavxc']

# РЕШЕНИЕ 1, через встроенный метод ----------------------------------------------------------------
# print(eval('1+2*3')) № 7 # Встроенный метод в Python
# -------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 2, используя операции +,-,/,*. приоритет операций стандартный.---------------------------
# -------------------------------------------------------------------------------------------------
# my_string = '1 - 2 * 3'.split() # При помощи .split() сделал из строки список строк, по 'пробелу'
# for i in range(len(my_string)):
#     if my_string[i].isdigit():
#         my_string[i] = int(my_string[i]) # каждый элемент списка строк делаю числами.
# print(my_string) # [1, '-', 2, '*', 3] # список строк
# operator_1 = {'+': lambda x, y: x + y, # Создал словарь.
#             '-': lambda x, y: x - y}
# operator_2 ={'*': lambda x, y: x * y,
#             '/': lambda x, y: x / y} 

# index = 0 # Счетчик
# while ('*' in my_string) or ('/' in my_string): # Проверяю, есть ли '*' или '/' в 
#     if my_string[index] in operator_2:
#         temp = operator_2[my_string[index]](my_string[index - 1], my_string[index + 1])
#         del my_string[index - 1: index + 2] # del - удаляет элементы из списка my_string[от index-1 до index+2]
#         my_string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1 # Если operator отсутствует, я иду по списку дальше.

# index = 0
# while '+' in my_string or '-' in my_string:
#     if my_string[index] in operator_1:
#         temp = operator_1[my_string[index]](my_string[index - 1], my_string[index + 1])
#         del my_string[index - 1: index + 2]
#         my_string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1
        
     
# print(my_string)
# print(eval('1 - 2 * 3')) # Встроенная функция.

# ---------------------------------------------------------------------------------------------------
# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# --------------------------------------------------------------------------------------------------

# incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
# outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1] 
# # Иду по (incoming_list) и если (i) элемент встречается только один раз (incoming_list.count(1) == 1, то 
# # добавляю его в (outcoming_list)
# print(outcoming_list) # [2, 10]
# # --------------------------------------------------------------------------------------------------
# # РЕШЕНИЕ 2 через фильтр ----------------------------------------------------------------------------

# outcoming_list2  = list(filter(lambda x: incoming_list.count(x) == 1, incoming_list))
# print(outcoming_list2) # [2, 10]

