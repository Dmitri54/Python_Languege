# 5. Реализуйте алгоритм перемешивания списка.
# ---------------------------------------------------------------------------------------------------------
# import random

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = random.shuffle(list)
# print(list)

# ==========================================================================================================
# import random

# list_len = int(input('Введите длину списка: '))
# my_list = []
# for q in range(0, list_len):
#     my_list.append(input('Заполните ячейку списка: '))
# list_index = []
# for i in range(0, list_len):
#     list_index.append(i)
# mix_index = random.sample(list_index, list_len)
# mix_index[:] = list(map(int, mix_index))
# k = 0
# new_list = []
# for n in range(0, list_len):
#     new_list.append(my_list[mix_index[k]])
#     k += 1
# print(f'{my_list} --> {new_list}') # ['1', '2', '3', '4'] --> ['1', '2', '4', '3']

