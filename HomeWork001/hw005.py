# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# -----------------------------------------------------------------------------------------------
print('Программа запрашивает координаты двух точек и выводит расстояние между ними.')
import math
print('Введите координаты точки А и нажмите Enter.')
x1 = float(input("X: "))
y1 = float(input("Y: "))
print('Введите координаты точки B и нажмите Enter.')
x2 = float(input("X: "))
y2 = float(input("Y: "))
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('-> {:.2f}'.format(a), sep='')
