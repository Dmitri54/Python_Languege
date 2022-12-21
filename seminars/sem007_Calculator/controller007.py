# controller.py - модуль дирижёр, собирает все в кучу и заставляет работать.

from view007 import operator, numbers, print_result
from data_base007 import write_data, read_data, write_data_result
from funcs007 import do_it

def click():
    x = numbers()
    y = numbers()
    z = operator()
    
    write_data(x, y, z)
    result = do_it(read_data())

    write_data_result(result)
    print_result(result)

