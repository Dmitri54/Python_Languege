# Метод, для xml представления

from user_interface02 import temperature_view
from user_interface02 import wind_speed_view
from user_interface02 import pressure_view

# Чтобы не использовать втроенные библиотеки, я описал метод.
def create(device = 1): # Метод - получает значение с первого элемента, 
    xml = '<xml>\n' # xml представление.
    xml += '   <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device)) # Обычная строка, которая форматируется и значение температуры.
    xml += '   <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device)) # Значение ветра
    xml += '   <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device)) # Значение давления
    xml += '</xml>'

    with open('data.xml', 'w') as page: # Создаю фаил и его сохраняю.
        page.write(xml)
    return xml

def new_create(data, device = 1): # Метод - получает значение с первого элемента.
    t, p, w = data
    t = t * 1.8 + 32 # Чтобы было ы Фаренгейтах
    xml = '<xml>\n' # xml представление.
    xml += '   <temperature units = "f">{}</temperature>\n'\
        .format(t) # Обычная строка, которая форматируется и значение температуры.
    xml += '   <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w) # Значение ветра
    xml += '   <pressure units = "mmHg">{}</pressure>\n'\
        .format(p) # Значение давления
    xml += '</xml>'

    with open('new_data02.xml', 'w') as page: # Создаю фаил и его сохраняю.
        page.write(xml)
    return data