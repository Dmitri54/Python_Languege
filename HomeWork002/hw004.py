# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
# ===========================================================================================================

num = int(input('Введите число и нажмите Enter: '))
list = []
print('Сформированный список: ')
for i in range(-num, num + 1):
    list.append(i)
    print(i, end = ", ")
print('\n')
strRequest = input('Введите позиции элементов через пробел: ')
strIndex = (strRequest.split(' '))
answer = 1
for i in range(0, len(strIndex)):
    answer *= list[int(strIndex[i])]
print(f'Произведение элементов = {answer}')