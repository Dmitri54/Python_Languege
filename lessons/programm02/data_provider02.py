# Модуль, который будет поставлять данные

from random import randint # Подключил модуль, для генерации случайных чисел.

def get_temperature(sensor): # Функция отвечает за температуру.
    return randint(-20,0) if sensor else randint(0, 20)

def get_preassure(sensor): # Функция отвечает за давление.
    if sensor:
        return randint(720, 750) # диапазон ртутного столба.
    else:
        return randint(750, 770)
        

def get_wind_speed(sensor): # Функция отвечает за скорость ветра.
    if sensor == 1:
        return randint(0, 30) # Скорость ветра.
    else:
        return randint(30, 50)


# Опишу метод, который будет получать на вход Цельсии, а на выходе Фаренгейты.
# Собирать данные со всех датчиков и отдавать их одной порцией.
def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))

