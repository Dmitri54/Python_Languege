# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ----------------------------------------------------------------------------------------------------
# def foo(x):
#     return (2 * x) ** 2 + 4 * x + 5

# n = int(input('Введите k: ')) # 2
# print(foo(n)) # 29
# -----------------------------------------------------------------

# n = int(input())
# koef = [int(elem) for elem in input().split()]
 
# koef.append(koef[-1])
 
# for i in range(n, 0, -1):
#     koef[i] += koef[i-1]
        
# print(*koef)

# with open('/Users/User/Desktop/Python_Language/home_Work_04/file_hw04_hW04.txt', 'a') as f:
#     f.write(int(*koef))

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.