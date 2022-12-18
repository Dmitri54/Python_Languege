#  Модуль, для запуска программы (точка входа)

import html_creater02 as hc
import xml_generator02 as xg
import data_provider02 as dp

# print(hc.create()) # Делаю вызов метода.
# print(xg.create)

hc.new_create(xg.new_create(dp.data_collection())) # Чтобы вызвать метод комментирую (#) print(hc.create())
# dp.data_collection() - получение данных, далее мне нужно его пробросить 
# в метод отвечающий за xml генерацию xg.new_create(). 
