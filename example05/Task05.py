# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату первой точки x1: '))
y1 = int(input('Введите координату первой точки y1: '))
x2 = int(input('Введите координату второй точки x2: '))
y2 = int(input('Введите координату второй точки y2: '))
print(((x1 - x2)**2 + (y1 - y2)**2)**0.5)
