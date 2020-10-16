#функцию, которая в зависимости от выбора пользователя вычисляет площадь круга, прямоугольника или треугольника.
#Для вычисления площади каждой фигуры должна быть написана отдельная функция

import math
def triangle():
    a = int(input('Введите основание треугольника: '))
    h = int(input('Введите высоту треугольника: '))
    s = 0.5*a*h
    return s
def rectangle():
    a = int(input('Введите сторону прямоугольника: '))
    b = int(input('Введите сторону прямоугольника: '))
    s = a*b
    return s
def circle():
    r = int(input('Введите радиус круга: '))
    s = math.pi*r*r
    return s
choice = (input("Название фигуры = "))
if (choice == 'треугольник'):
    print(triangle())
if (choice == 'прямоугольник'):
    print(rectangle())
if (choice == 'круг'):
    print(circle())

