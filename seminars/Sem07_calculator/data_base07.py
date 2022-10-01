# Модуль отвечает за работу с файлом, открытие файла, для чтение и записи данных.

path = r'/Users/User/Desktop/Python_Language/seminars/Sem07_calculator/file07.txt'
path_log = f'/Users/User/Desktop/Python_Language/seminars/Sem07_calculator/log.txt'
def get_info():
    with open(path, 'r') as data: # r - открытие для чтения данных.
        data = data.read().split(' ')
    return data


def save_info(a):
    a = str(a)
    with open(path, 'w') as data: # w - открытие для записи данных.
        data.write(a)

def save_result(a):
    a = str(a)
    with open(path, 'a') as data: # a - открытие для добавления данных.
        data.write(f'\nyour result = {str(a)}')
    return data

def log(a, b):
    with open(path_log, 'a') as data: # a - открытие для добавления данных.
        data.write('\nyour equation: {} {} {} = {}'.format(a[0], a[1], a[2], b))