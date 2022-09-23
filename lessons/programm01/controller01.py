# Данный модуль связывает мужду собой model04.py и view04.py
# В рамках этого модуля, у пользователя будет кнопка, которую он сможет нажимать.

from unittest import result
# import model_sum01 as model01# Импортирую (связываю) файлы кода.
# import model_mult01 as model01
import model_sub01 as model01
import view01


def button_click(): # Метод позволит создать кнопку, которую может нажимать пользователь.
    value_a = view01.get_value() # Запрос на получение данных у пользователя
    value_b = view01.get_value()
    model01.init(value_a, value_b) # Инициализация данных
    result = model01.do_it() # Вычисление суммы
    view01.view_data(result, 'result') # Отображение результата.
