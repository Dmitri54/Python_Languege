# В этом Модуле находится основная логика программы.
# Что запрашиваю, кому отдаю, что получаю.


import gui07
import data_base07
import check07

def start():
    data_base07.save_info(gui07.get_input()) # Запрашиваю через .get_input() три строки.
    # Строка возвращается и записывает в Метод data_base07 функция .save_info, т.е. запись в фаил.
    data = data_base07.get_info() # Читаю фаил со строками, сохраняю значение в переменную data.
    result = check07.check(data) # Перадаю переменную data в Метод check07 функция check
    data_base07.save_result(result) # Полученный result передаю в Метод data_base07 функция save_result. Сохранил result.
    gui07.send__info(result) # Передаю result в Метод gui07 функция send__info - выведет сообщение пользователю.
    data_base07.log(data, result) # Сохраняет все значения data и result в отдельном файле.
