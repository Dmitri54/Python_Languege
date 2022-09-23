#  Модуль, для запуска программы (точка входа)

import html_creater02 as hc
import xml_generator02 as xg
import data_provider02 as dp

# print(hc.create())
# Вывод 1:
# htmi>
#   <head></head>
#   <body>
#    <p style="front-size:30px;">Temperature: -7 c</p>
#    <p style="front-size:30px;">Wind_speed: 8 c</p>
#    <p style="front-size:30px;">Pressure: 749 c</p>
#    </body>
# </html>
# print(xg.create())
# Вывод 2:
# -//- Вывод 1, далее вывод 2.
# <xml>
#    <temperature units = "c">-17</temperature>
#    <wind_speed_view units = "m/s">26</wind_speed_view>
#    <pressure units = "mmHg">743</pressure>
# </xml>
hc.new_create(xg.new_create(dp.data_collection()))
