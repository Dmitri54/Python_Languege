# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# ----------------------------------------------------------------------------------------------

quarter = int(input('Введите четверть: '))

def Coord(x):
    if (x == 1):
        print(f'Диапазон возможных координат {x} четверти: X > 0 и Y > 0')
    elif (x == 2):
        print(f'Диапазон возможных координат {x} четверти: X < 0 и Y > 0')
    elif (x == 3):
        print(f'Диапазон возможных координат {x} четверти: X < 0 и Y < 0')
    elif (x == 4):
        print(f'Диапазон возможных координат {x} четверти: X > 0 и Y < 0')
    else:
        print('Введина не корректная четверть.')

quarterRes = Coord(quarter)