# Урок 4. Python: от простого к практике.
# Задача 0. Написать программу сложения двух чисел.
# --------------------------------------------------------------------------------------
# Простые решения: --------------------------------------------------------------------
# 1 Просто запросит у пользователя и сложит в принте-----------------------------------
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {x + y}')
# 2 Через функцию-------------------------------------------------------------------------
# def sum(a, b):
#  return a + b
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {sum(x, y)}')
# 3 Через lambda ---------------------------------------------------------------------------
# sum = lambda a, b: a + b
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {sum(x, y)}')
# 4 ------------------------------------------------------------------------------------
# Написать программу, которое выглядит как приложение. Пройдя от создания блок схемы, описать модули, 
# что в них будет ханиться и как связать всё воедино. Описать как именно будет выглядеть приложение.
# ---------------------------------------------------------------------------------------------------
# Решение преподователя: ----------------------------------------------------------------------
# Проектирование приложения. ------------------------------------------------------------------------
# Далее пришу код, folder programm01, file model04.py, view04.py, controller04.py

# main04.py - это точка входа, для рабоьы программы.

# ---------------------------------------------------------------------------------------------------
# Идея: совместная разработка
# Система собирает информацию с датчиков, в ней есть модуль логирования, который заносит в журнал 
# все обращения к датчикам. В системе есть модуль, выполняющий обращения для получения данных с 
# датчиков и модуль генерации htmlпредставления. Запуск системы осуществляется из головного модуля.
# -------------------------------------------------------------------------------------------------- 
# Задача: Описать модули и что они делают
# РЕШЕНИЕ преподователя:---------------------------------------------------------------------------
# Будет 5 модулей
# Модуль 1: сбор информации с датчиков
# Модуль 2: логирование
# Модуль 3: UI
# Модуль 4: HTML-генератор
# Модуль 5: главный модуль
# ------------------------------------------------------------------------------------------------
# Так будут называться модули
# Модуль 1: data_provider
# Модуль 2: logger
# Модуль 3: user_interface
# Модуль 4: html_creater
# Модуль 5: main
# -----------------------------------------------------------------------------------------------
# Далее в рамках каждого модуля я опишу набор методов.
# data_provider
#    get_temperature, get_pressure, get_wind_speed # Метод позв. получить температуру, давление, скорость ветра. 
# logger
#    temperature_logger, pressure_logger, wind_speed_logger # Метод позв. логировать отдельно информацию о температуре, давление, скор. ветра.
# user_interface
#    temperature_view, pressure_view, wind_speed_view # Метод выводит информацию в интерфейс пользователя.
# html_creater
#    create # Метод, будет одна кнопка, для создания этого представления, а дальше можно передать или использовать в своей системе.
# main # Метод, чтобы запустить систему. 
# Далее пишу код.------------------------------------------------------------------------------------
# Создал папку programm02
# Creat: file data_provider02.py, logger02.py, user_interface02.py, html_creater02.py, main02.py
# Далее запускаю программу, создается file index.html и log.csv
# Если открыть index.html правым кликом в браузере, то будет отображение информации.
# В file log.csv - будет сохраняться и перезаписяваться информация с датчиков, храниться в файле excel
# Далее создал xml_generator02.py - что по другому отображать.
# Дальше 


