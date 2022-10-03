# Модуль с функциями программы.

import csv


path = r'/Users/User/Desktop/Python_Language/seminars/Sem08_telephone_directory/data08.csv'

def add_info(): # Функция запрашивает у пользователя Имя и телефон, добавляет их в фаил
    name = input('Имя: ')
    phone = input('Телефон: ')
    newLine = [name, phone]
    with open(path, 'a', newline = '') as data: # a - открытие для добавления данных.
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(newLine)


def find_num(): # Функция выдает номер телефона по введенному имени.
    name = input('Имя: ')
    with open(path, 'r') as file: # r - открытие для чтения данных.
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            if name == row[0]:
                print(*row)


def delete_item():
    name = input('Какую запись вы хотите удалить? ')
    temp_list = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        print(reader)
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if name in item:
            temp_list.remove(item)
            print('Запись удалена.')
            break  
    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(temp_list) 

        
def show_all():
    with open(path, 'r') as file: # r - открытие для чтения данных.
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            print('{:<10} {:<15}'.format(*row))



