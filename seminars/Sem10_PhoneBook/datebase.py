from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

def contact_list(): # Функция показывает контакт
    cursor.execute('select * from phonebook')
    return cursor.fetchall()


def add_contact(): # Функция добавляет контакт
    cursor.execute('insert info phonebook'
                   '(last_name, name, phone)'
                   'values (?, ?, ?);', lst)
    connection.commit()