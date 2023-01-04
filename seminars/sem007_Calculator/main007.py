# Урок 7. Python: от простого к практике
# =================================================================================================
# Двумерный массив, это список со списками в Pyhton
# a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(a)

# b = [[i for i in range(3)] for x in range(3)]
# print(b)
# ==================================================================================================
# Программа калькулятор (+, -, *, /).
# ---------------------------------------------------------------------------------------------------
# Пишу программу. 
# Сначала опишу модули и что они делают:
# 
# main.py - главный модуль, для запуска программы (точка входа).
# controller.py - модуль дирижёр, собирает все в кучу и заставляет работать. 
# view.py - будет заниматься выводом и вводом данных в консоль (input(), print()).
# data_base.py - база данных. Хранит значения, которые вводил пользователь.
# funcs.py - модуль с функциями, для решения.


# Логика работы: 
# Запуск main.py, controler.py запросит у view.py информацию, view.py передаст controler.py, 
# controller.py передаст data_base.py и funcs.py, funcs.py передаст результат решения в controler.py,
# controller.py передаст view.py и data_base.py.

from controller007 import click

click()

# Для запуска в терминале захожу в папку sem007_Calculator, далее в тетмирале пишу: python main007.py