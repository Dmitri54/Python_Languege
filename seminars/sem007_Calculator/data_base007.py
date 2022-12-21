from pathlib import Path # Так лучше. Запуск прогаммы нужно выполнять из папки sem007_Calculator, коммандой python main007.py


def write_data(num1, num2, operator):
    d = Path('our_data007.txt')
    with open(d, 'w') as data:
        a = f'{num1} {num2} {operator}'
        data.write(a)

def read_data():
    d  = Path('our_data007.txt')
    with open(d, 'r') as data:
        return data.read().split()

def write_data_result(result):
    d  = Path('our_result007.txt')
    with open(d, 'w') as data:
        return data.write(str(result))