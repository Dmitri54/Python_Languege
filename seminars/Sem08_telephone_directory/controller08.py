# Метод в котором собираю и отлаживаю программу.

import user_input08
import funcs08

user_choice = user_input08.menu() # Сохранил в переменную user_choice, результат вызова функции .menu().
if user_choice == '1':
    funcs08.add_info()
elif user_choice == '2':
    funcs08.find_num()
elif user_choice == '3':
    funcs08.delete_item()
elif user_choice == '4':
    funcs08.show_all()

