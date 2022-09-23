# Модуль, который отвечает за работу с user interface

import data_provider02 as prov
import logger02 as log

def temperature_view(sensor): # Метод покажет информацию о погоде. senson - это более точные настройки, для системы
    data = prov.get_temperature(sensor) # Опишу получение данных, забираю у prov. и вызываю соответствующий метод, передовая значения sensor 
    log.temperature_logger(data) # Далее, запишу в log. информацию о том значении, которое я получил.
    return data # Верну те значения, которые я получил.

def pressure_view(sensor): # Метод покажет информацию о давления
    data = prov.get_preassure(sensor)  
    log.pressure_logger(data) 
    return data 

def wind_speed_view(sensor): # Метод покажет информацию о скорости ветра
    data = prov.get_wind_speed(sensor)  
    log.wind_speed_logger(data) 
    return data  
