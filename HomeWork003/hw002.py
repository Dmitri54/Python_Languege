# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# =========================================================================================================

def mut_elem(list):
        if (len(list) % 2 == 0):
                ten = (len(list) // 2)
        else:
                ten = (len(list) // 2) + 1
        newList = []
        for i in range(0, ten):
            num = list[i] * list[ten - i + 1]
            newList.append(num)
        if (len(list) % 2 != 0):
            newList[ten - 1] = list[ten - 1]
        return newList

    
resultList = [2, 3, 4, 5, 6, 7]

print(mut_elem(resultList)) # [12, 15, 16]

