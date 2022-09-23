# Модуль logger 

from datetime import datetime as dt
from time import time

def temperature_logger(data): # Функция(метод) - отвечает за логирование температуру.
    time = dt.now().strftime('%H:%M') # Чтобы получить time мне нужно обратиться к модулю dt.now() / .strftime() - встроенный метод позволяет выводить время в строке. ('%H:%M') - маска, для 
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n' # Первым аргументом будет время, температура и вторым значением будет выступать значение которое придет в метод.
                     .format(time, data)) 

def pressure_logger(data): # Функция(метод) - отвечает за логирование давления.
    time = dt.now().strftime('%H:%M') 
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n' 
                     .format(time, data)) 


def wind_speed_logger(data): # Функция(метод) - отвечает за логирование скорости ветра.
    time = dt.now().strftime('%H:%M') 
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n' 
                     .format(time, data))


