# Модуль отвечает за проверку элемента строки.

import functions07


def check(data):
    # if data[1] == '+':
    #     return functions07.sum(data[0], data[2])
    # elif data[1] == '-' :
    #     return functions07.minus(data[0], data[2])
    # elif data[1] == '*':
    #     return functions07.mult(data[0], data[2])
    # elif data[1] == '/':
    #     return functions07.dev(data[0], data[2])
    # else:
    #     print('Wrong equation sign!')
    match data[1]: # С match case - работает быстрее.
        case '+':
            return functions07.sum(data[0], data[2]) # Если второй элемент содержит нужный знак, то 
        # вызывается Метод functions07 функция .sum 
        case '-':
            return functions07.minus(data[0], data[2])
        case '*':
            return functions07.mult(data[0], data[2])
        case '/':
            return functions07.dev(data[0], data[2])
        case _:
            print('Wrong equation sign!') # Это сообщение будет в консоле
            return 'Wrong equation sign!' # Это будет сохранено в файле log.txt


