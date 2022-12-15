# Урок 3. Ускоренная обработка данных: 
# lambda, filter, map, zip, enumerate, list comprehension
# --------------------------------------------------------------------------------------------------
# Анонимные, lambda функции:
# def sum(x):
#     return x+10 # x+22  # x+242

# def mult(x):
#     return x**2 # x**3  # x**5

# sum(mult(2)) 
# Чтобы не описывать в явную функции, которые используются только один раз,
# можно использовать анонимные lambda функции.
# =========================================================================================================
# def f(x):
#     x**2       # Возведение числа в квадрат.
# g = f          # Передаю функцию f в переменную g.
# print(f(1))    # None
# print(type(f)) # <class 'function'>
# print(g(1))    # None
# -----------------------------------------------------------------------------------------------------------
# Так как можно функцию положить в переменную, значит я могу в качестве аргумента какой-то функции передать функцию.
# def f(x):
#     return x**2
# print(f(2)) # 4 
# ---------------------------------------------------------------------------------------------------------
# К примеру:
# Я использовал (делал вызов) функцию один раз, вопрос как можно сократить код?
# Можно соократить код, передав в переменную функцию.
# ---------------------------------------------------------------------------------------------------------
# g = f # Положил (передал) функцию в переменную. Работать она будет так же как f.
# # т.е. у меня есть переменная, которая хранит в себе ссылку на функцию.
# print(type(f)) # <class 'function'>
# print(type(g)) # <class 'function'>
# print(f(4))    # 16
# print(g(4))    # 16
# ---------------------------------------------------------------------------------------------------
# Пример с одной переменной:-------------------------------------------------------------------------
# def calc1(x):
#     return x+10
# print(calc1(10)) # 20

# def calc2(x):
#     return x*10
# print(calc2(10)) # 100
# Если у меня есть функция, которая занимается только складыванием чисел, то можно написать функцию, 
# в которую будет приходить некий орератор и число.
# ---------------------------------------------------------------------------------------------------
# def math(op, x): # В качестве аргумента будет приходить операция и какое то число. 
# op - функция, в которую я передаю аргумент и она считает.
#     print(op(x))
# math(calc2, 10) # 100
# math(calc1, 10) # 20
# ---------------------------------------------------------------------------------------------------
# Пример с двумя переменными:------------------------------------------------------------------------
# def sum(x, y):
#     return x+y
# f = sum
# f = lambda q, w: q+w 
# sum = lambda x, y: x+y # Это тоже самое, что и выше на три строчки!!!
# # А дальше можно пропустить шаг создание отдельной переменной и сразу в качестве аргумента пробрасывать lambda.
# def mult(x, y):
#     return x*y

# def calc(op, a, b): # Функция, которая принимает функцию и два аргумента.
#     print(op(a, b)) # Так выведет на экран.
#     # return op(a, b) # Можно и так делать возврат значения.

# # calc(mult, 4, 5) # 20
# # calc(f, 4, 5) # 9 
# # calc(sum, 4, 5) # 9
# calc(lambda x, y: x+y, 4, 5) # 9 
# ====================================================================================================
# list Comprehension - Нужен он, чтобы быстро создавать списки.
# [exp for item in iterable]
# [exp for item in iterable (if conditional)] # Создание списка по условию
# [exp <if conditional> for item in iterable (if conditional)]
# Разберу первый пример написания [exp for item in iterable]
# ---------------------------------------------------------------------------------------------------
# Допустим, мне нужно создать список четных чисел в диапозоне от 1 до 100.---------------------------
# ---------------------------------------------------------------------------------------------------
# list = [] # Создаю список, для хранения данных
# for i in range(1, 101): # Запускаю цикл, бегу от 1 до 101.
#     if(i%2 == 0): # Выборка идет только четных чисел. # покажет все числа от 1 до 100.
#         list.append(i) # Добавляю элемент в список 
# print(list) # покажет только четные числа (list)
# ---------------------------------------------------------------------------------------------------
# Таже самая конструкция только короче, но без условия (if(i%2 == 0)) ------------------------------
# list = [i for i in range(1, 101)] # Запись в одну строку.
# print(list) # покажет все числа от 1 до 100.
# С условием!!!======================================================================================
# list = [i for i in range(1, 101) if i%2 == 0] 
# print(list) # покажет только четные числа
# ---------------------------------------------------------------------------------------------------
# Допустим, мне нужно создать пару каждого из чисел, т.е. подключаю КОРТЕЖИ.
# list = [(i, i) for i in range(1, 101) if i%2 == 0] 
# print(list) # покажет список кортежей. # [(2, 2), (4, 4),...(98, 98), (100, 100)]
# ---------------------------------------------------------------------------------------------------
# Так же можно обрабатывать данные, т.е. указывать не просто само значение аргумента, 
# а взять какую нибудь функцию. Пример:
# def f(x):
#     return x**3 # Возведение в степень.
# list = [f(i) for i in range(1, 101) if i % 2 == 0]
# print(list) # Возведение четных значений в степень. # [8, 64,...941192, 1000000]
# ---------------------------------------------------------------------------------------------------
# Для наглядности подключу КОРТЕЖИ:
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 101) if i % 2 == 0]
# print(list) # Число и его куб # [(2, 8), (4, 64),..(100, 1000000)]
# ====================================================================================================
# Подлючу lambda.
# ЗАДАЧА: В файле храняться числа, нужно выбрать четные 
# и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить КОРТЕЖИ:
# [(2, 4), (8, 64), (38, 1444)]
# РЕШЕНИЕ---------------------------------------------------------------------------------
# path = '/Users/User/Desktop/Python_Language/lessons/file.txt' # Важно!!! Обращать внимание на мелочи. Путь к файлу.
# f = open(path, 'r') # r - read - чтение.
# data = f.read() + ' ' # Это хитрость (искуственный прием). 
# # Считываю все, что есть в строчке и искуственно добавляю пробел, для логики, которая ниже описана.
# f.close() # Закрываю фаил.

# numbers = [] # Создал список, в который буду наполнять.
# while data != '': # Пробегаю по всей строке (data) и делаю проверку пока моя строка не пустая. 
#     space_pos = data.index(' ') # Дальше моя задача, найти первую позицию пробела, 
#     numbers.append(int(data[:space_pos])) # Взять всё что находиться, от первого символа до позиции 
#     # первого пробеза и превратить это в число, и добавить в список чисел(numbers).
#     data = data[space_pos + 1:] # Обновить строку, с учётом того, что, то что уже проверено, больше проверять не нужно.
# out = [] # Создаю новый список.
# for e in numbers: # Пробегаю по списку (numbers).
#     if not e % 2: # Проверяю условие, что число является четным.
#         out.append((e, e ** 2)) # Добавляю в новый список кортежа, где первая координата (e) - само число, (e**2) - квадрат этого числа. 
# print(out) # [(2, 4), (8, 64), (38, 1444)]
# ----------------------------------------------------------------------------------------------------
# Переписал код, с использованием lambda и list Comprehension.
# ----------------------------------------------------------------------------------------------------
# def select(f, col): # Начну с описания функции (select), которая принимать функцию и набор данных.
#     return [f(x) for x in col] # Формирую новый список и сразу его возвращают.

# def where(f, col): # Функции (where), которая принимать функцию и набор данных.
#     return [x for x in col if f(x)] # Формирую новый список и сразу его возвращают.

# data = '1 2 3 5 8 15 23 38'.split() # В данном случае .split() - позволяет получить набор строк.

# res = select(int, data) 
# # Создал новый список (res), в неё буду складывать результат работы функции (select()), 
# # в которую будет передоваться функция (int) и аргумент (data)
# res2 = where(lambda x: not x%2, res)
# # В список (res) положу результат работы функции (where), в которую запишу функцию проверки (lambda x: not x%2,)
# # и в качестве второго аргумента я передаю результат работы на передыдущем этапе.
# res3 = select(lambda x: (x, x**2), res2)
# # Создам переменную, вызову функцию (select), в которую передам функцию (lambda x: (x, x**2)) - принимающую (x)
# # и возвращающую КОРТЕЖ (x, x**2). В качестве второго аргумента будет результат работы на предыдущем этапе
# print(res) # [1, 2, 3, 5, 8, 15, 23, 38]
# print(res2) # [2, 8, 38]
# print(res3) # [(2, 4), (8, 64), (38, 1444)]
# ==========================================================================================================
# Простые функции типо (select, where), есть в Python!!!
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с новыми объектами.
# f(x) -> x + 10
# map(f, [1, 2, 3, 4, 5])
#         ↓  ↓  ↓  ↓  ↓ 
#       [11, 12, 13, 14, 15]
# Нельзя пройтись дважды
# Пример: -----------------------------------------------------------------------------------------
# li = [x for x in range(1, 20)] # Создам список (li), в который помещу целые числа.
# print(li) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# # Я хочу получить новый набор данных через функцию (map): ------------------------------------------
# li1 = list(map(lambda x: x+10, li)) # Пишу (map), в качестве первого аргумента буду передовать (lambda x: x+10)
# # а в качестве второго аргумента набор данных. Для того, чтобы получить набор данных нужно превратить 
# # в список, пишу в начале (list()).
# print(li1) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# ======================================================================================================
# Пример:-------------------------------------------------------------------------------------------
# Допустим, с квавиатуры вводятся числа, в качестве разделителя пробел.-----------------------------
# --------------------------------------------------------------------------------------------------
# data = list(map(int,input('Введите числа через пробел: ').split())) # Пишу input() - входную строку. Далее склею строки по пробелу.
# # input().split() - тут я получаю список, который буду пробрасывать в функцию (map(int, input().split()))
# # в качестве аргумента буду передовать функцию (int) - превращающую лист из строк в лист чисел. 
# # А что бы получить набор данных пишу в начале (list()).
# print(f'Лист чисел: {data}') # [1, 2, 3, 45, 67]
# ---------------------------------------------------------------------------------------------------
# Можно не писать list (приведение к типу), а сразу пробежаться по объектам
# data = map(int,input('Введите числа через пробел:').split()) # Строка распарсится на элементы и превратится в числа.
# data = map(int, '1 2 3 4 555 6'.split()) # Чтобы каждый раз не вводить. 
# data = list(map(int, '1 2 3 4 555 6'.split())) # Тут я работаю с сохраненными данными. 
# for e in data:
#     print(e)
# print('--') # Вывод разделителя (--)

# for e in data:
#     print(e) # Печатае в столбик, каждый элемент с новой строки.
# Результат работы функции (map) это итератор. По итератору можно пробежать, только один раз.
# Поэтому, чтобы работать с одними и теме же данными, я должен их где-то сохранить, пишу (list()).
# ----------------------------------------------------------------------------------------------
# Пример кода, который писал выше, но короче:------------------------------------------------------
# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 8 23 38'.split()

# res = map(int, data)
# res1 = where(lambda x: not x % 2, res)
# res2 = list(map(lambda x: (x, x**2), res1))
# print(res) # <map object at 0x000001D8B376BE20>  - Нужно писать (list()), чтобы получить список.
# print(res1) # [2, 4, 8, 38]
# print(res2) # [(2, 4), (4, 16), (8, 64), (38, 1444)]
# =================================================================================================
# Что бы избавиться от функции (where) в Python есть функция filter.
# ---------------------------------------------------------------------------------------------
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.
# f(x) -> x  - чётное
# filter(f, [1, 2, 3, 4, 5])
#               ↓     ↓
#              [2,    4]
# Нельзя пройтись дважды.
# -------------------------------------------------------------------------------------------------
# Пример применения функции filter:-------------------------------------------------------------------
# data = [x for x in range(10)] # Зделаю список, от 0 до 9
# print(data) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = list(filter(lambda x: not x % 2, data)) # Сделаю выборку элементов, которые четные.
# print(res) # [0, 2, 4, 6, 8]
# ---------------------------------------------------------------------------------------------------
# Пример кода с использованием map, filter:--------------------------------------------------------------------------------------------
# data = '1 2 3 4 5 8 23 38'.split()
# res = map(int, data)
# res1 = filter(lambda x: not x % 2, res)
# res2 = list(map(lambda x: (x, x**2), res1))
# print(res) # <map object at 0x000002A5C6F4BEE0>
# print(res1) # <filter object at 0x000002A5C6F4BEB0>
# print(res2) # [(2, 4), (4, 16), (8, 64), (38, 1444)]
# =======================================================================================================
# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с 
# кортежами из элементов входных данных.
# Пример:------------------------------------------------------------------------------------------
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't']) # передаю некие наборы данных
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')] # На выходе вижу компановку по индексам, 
# в виде КОРТЕЖА, приведенного к списку.
# Нельзя пройтись дважды
# Пример:------------------------------------------------------------------------------------------
# users = ['user1', 'user2', 'user3', 'user4', 'user5'] # Первый набор данных
# ids = [4, 5, 9, 14, 7] # Второй набор данных.
# salary = [111, 222, 333] # Третий набор данных.
# # data = list(zip(users, ids)) 
# Пишу функцию (zip()), в качестве первого аргумента передаю список (users) и (ids). 
# Чтобы получить список пишу в начеле (list()).
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# Функция (zip()) пробегает по минимальному входящему набору. Т.е. если у меня появиться новый набор 
# данных, которые нужно также подмешать к исходным.
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
# ------------------------------------------------------------------------------------------------
# Если мне потребуется пронумеровать мой список, я могу взять два исходных и попорядку через range 
# подмешать zip и просчитать, но есть уже готовая функция в Python enumerate().
# ===============================================================================================
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#                         ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды 
# -----------------------------------------------------------------------------------------------
# Пример:----------------------------------------------------------------------------------------
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(enumerate(users)) # enumerate - пронумерует переданный список данных (users).
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

