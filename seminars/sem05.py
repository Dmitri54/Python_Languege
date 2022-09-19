# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# ---------------------------------------------------------------------------------------------
# Задача 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.
# 1 2 4 5
# --------------------------------------------------------------------------------------------

# f1 = open('/Users/User/Desktop/Python_Language/seminars/file_sem05.txt', 'r')
# output1 = f1.read()
# nlist = output1.split(' ')
# print(nlist) # ['1', '2', '3', '4', '6', '7']

# for i in range(1, len(nlist)):
#     if int(nlist[i]) - 1 != int(nlist[i - 1]):
#         numb = int(nlist[i]) - 1
  
# print(numb) # 5
# -------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 2, короче код при помощи list comprehension
# --------------------------------------------------------------------------------------------------
# f1 = open('/Users/User/Desktop/Python_Language/seminars/file_sem05.txt', 'r')
# output1 = f1.read()

# nlist = output1.split(' ')
# print(nlist) # ['1', '2', '3', '4', '6', '7']

# mylist = [int(nlist[i]) - 1 for i in range(1, len(nlist)) if int(nlist[i]) - 1 != int(nlist[i - 1])]
# print(mylist) # [5]
# ----------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 3 обычное решение и при помощи list comprehension.

# with open('/Users/User/Desktop/Python_Language/seminars/file_sem05.txt', 'r') as f:
#     string = f.readline()
# print(string) # 1 2 3 5 6 7
# string = string.split(' ')
# string = list(map(int, string))

# # for i in range(1, len(string)):
# #     if string[i] - 1 != string[i - 1]:
# #         print(f'Missed: {string[i] - 1}')
# #         break
# # else:
# #     print('Good') # Good, если все числа по порядку.

# lst = [(string[i] - 1) for i in range(1, len(string)) if string[i] - 1 != string[i - 1]]
# print(lst) # [4]

# -----------------------------------------------------------------------------------------------------
# Задача 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
# --------------------------------------------------------------------------------------------

# nlist = [1, 5, 2, 3, 4, 6, 1, 7]
# print(nlist) # [1, 5, 2, 3, 4, 6, 1, 7]
# count = 0

# mylist = [nlist[0]]
# for i in range(1, len(nlist)):
#     if nlist[i] > nlist[count]:
#         mylist.append(nlist[i])
#         count = i
# print(mylist) # [1, 5, 6, 7]
# ---------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 2 при помощи list comprehension.
# -------------------------------------------------------------------------------------------------

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# print(my_list) # [1, 5, 2, 3, 4, 6, 1, 7]
# count = 0

# new_list = ([my_list[i] for i in range(1, len(my_list)) if my_list[i] >= max(my_list[0:i])])
# new_list.insert(0, my_list[0]) # Добавляю первый элемент в начало.
# print(new_list) # [1, 5, 6, 7]

# -----------------------------------------------------------------------------------------------
# Задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример: 
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'
# ----------------------------------------------------------------------------------------------
# РЕШЕНИЕ обычное
# ---------------------------------------------------------------------------------------------
# test = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'
# index = 0

# my_list = test.split()
# print(my_list) # ['Мы', 'неабв', 'очень', 'любим', 'Питон', 'иабв', 'Джавабв']
# i = 0
# while i in range(len(my_list)):
#     if text_find in my_list[i]:
#         my_list.remove(my_list[i])
#     else:
#         i+= 1
# print(my_list) # ['Мы', 'очень', 'любим', 'Питон']
# ------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 2 при помощи list comprehension.
# ------------------------------------------------------------------------------------------------
# test = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'
# index = 0

# my_list = test.split()
# print(my_list) # ['Мы', 'неабв', 'очень', 'любим', 'Питон', 'иабв', 'Джавабв']

# new_list = [item for item in my_list if text_find not in item]

# print(new_list) # ['Мы', 'очень', 'любим', 'Питон']


