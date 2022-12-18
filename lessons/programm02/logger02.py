# Модуль logger 

from datetime import datetime as dt # т.к. при сохраниение информации нужна дата
from time import time # и нужно время

def temperature_logger(data): # Функция(метод) - отвечает за логирование температуру.
    time = dt.now().strftime('%H:%M') 
    # Чтобы получить time мне нужно обратиться к модулю dt.now() 
    # .strftime() - встроенный метод позволяет выводить время в строке. ('%H:%M') - маска отбражения времени.
    path = '/Users/User/Desktop/Python_Language/lessons/programm02/log_lec04.csv'
    with open(path, 'a') as file:
        file.write('{};temperature;{}\n' # Первым аргументом будет время, температура и вторым значением будет выступать значение которое придет в метод.
                     .format(time, data)) 

def pressure_logger(data): # Функция(метод) - отвечает за логирование давления.
    time = dt.now().strftime('%H:%M') 
    path = '/Users/User/Desktop/Python_Language/lessons/programm02/log_lec04.csv'
    with open(path, 'a') as file:
        file.write('{};pressure;{}\n' 
                     .format(time, data)) 


def wind_speed_logger(data): # Функция(метод) - отвечает за логирование скорости ветра.
    time = dt.now().strftime('%H:%M') 
    path = '/Users/User/Desktop/Python_Language/lessons/programm02/log_lec04.csv'
    with open(path, 'a') as file:
        file.write('{};wind_speed;{}\n' 
                     .format(time, data))


