# Модуль (html_creater), создающий html фаил.

from user_interface02 import temperature_view # Отдельно извлекаю методы (функции) из user_interface02.
from user_interface02 import wind_speed_view
from user_interface02 import pressure_view

# Чтобы не использовать втроенные библиотеки, я описал метод.
def create(device = 1): # Метод создания фаила html и записи в него. device = 1 - получает значение с первого элемента. 
    style = 'style="front-size:30px;"' # Тут описан стиль написания текста (22px or 30px)
    html = 'htmi>\n  <head></head>\n  <body>\n' # html представление.
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device)) # Обычная строка, которая форматируется и значение температуры.
    html += '   <p {}>Wind_speed: {} c</p>\n'\
        .format(style, wind_speed_view(device)) # Значение ветра
    html += '   <p {}>Pressure: {} c</p>\n'\
        .format(style, pressure_view(device)) # Значение давления
    html += '   </body>\n</html>'
    
    path = '/Users/User/Desktop/Python_Language/lessons/programm02/index.html'
    with open(path, 'w') as page: # Создаю фаил и его сохраняю.
        page.write(html)
    return html

def new_create(data, device = 1): # Метод - получает значение с первого элемента, 
    t, p, w = data
    style = 'style="front-size:30px;"' # Тут описан стиль написания текста (22px or 30px)
    html = 'htmi>\n  <head></head>\n  <body>\n' # html представление.
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t) # Обычная строка, которая форматируется и значение температуры.
    html += '   <p {}>Wind_speed: {} c</p>\n'\
        .format(style, w) # Значение ветра
    html += '   <p {}>Pressure: {} c</p>\n'\
        .format(style, p) # Значение давления
    html += '   </body>\n</html>'
    
    path = '/Users/User/Desktop/Python_Language/lessons/programm02/new_index02.html'
    with open(path, 'w') as page: # Создаю фаил и его сохраняю.
        page.write(html)
    return data
    