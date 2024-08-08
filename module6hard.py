"""
module6hard
"""
from math import pi

class Figure():
    def __init__(self, colors: tuple, sides_count=0):
        self.sides_count = sides_count
        self.__sides = []   # список сторон (целые числа)
        self.__color = []   # список цветов в формате RGB
        self.set_color(*colors)
        self.filled = False

    def get_color(self):
        """
        возвращает список RGB цветов
        """
        return self.__color

    def get_sides(self):
        """
        должен возвращать значение я атрибута __sides
        """
        return self.__sides

    def __is_valid_color(r, g, b):
        """
        служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
        перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа
        в диапазоне от 0 до 255 (включительно).
        """
        for _ in [r, g, b]:
            if not isinstance(_, int):
                return False
            if _ < 0 or _ > 255:
                return False
        return True

    def set_color(self, r, g, b):
        """
        принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        """
        if not Figure.__is_valid_color(r, g, b):
            return
        self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        """
        служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
        целые положительные числа и кол-во новых сторон совпадает с текущим,
        False - во всех остальных случаях.
        :return: True or False
        """
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int):
                return False
            if side < 0:
                return False
        return True

    def set_sides(self, *new_sides):
        """
        должен принимать новые стороны, если их количество не равно sides_count,
        то не изменять, в противном случае - менять.
        """
        if not Figure.__is_valid_sides(self, *new_sides):
            return
        self.__sides = []
        for iside in range(self.sides_count):
            self.__sides.append(new_sides[iside])

    def __len__(self):
        """
        должен возвращать периметр фигуры.
        """
        return sum(self.get_sides())

class Circle(Figure):
    def __init__(self, colors: tuple, *sides):
        super().__init__(colors, sides_count=1)
        arr = []
        if len(sides) == 1:
            arr.append(sides[0])
        else:
            arr.append(1)
        super().set_sides(arr)
        self.__radius = arr[0] / (2 * pi)

    def get_square(self):
        """
        возвращает площадь круга (можно рассчитать как через длину, так и через радиус)
        :return:
        """
        return pi * self.__radius ** 2

class Triangle(Figure):
    """
    Площадь треугольника вычисляется по формуле: S = 0.5 * a * h,
    где (a) – сторона треугольника, h – высота, построенная к стороне (а) . Из этого выражения найдите высоту: h = 2S/a.

    Если в условии даны длины трех сторон треугольника, найдите площадь по формуле Герона:
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5,
    где p – полупериметр треугольника; а, b, с – его стороны.
    Зная площадь, вы можете определить длину высоты к любой стороне
    """

    def __init__(self, colors, *sides):
        super().__init__(colors, sides_count=3)
        arr = []
        if len(sides) == 3:
            arr.append(sides[0]).append(sides[1]).append(sides[2])
        else:
            arr = [1] * 3
        super().set_sides(arr)
        p = sum(arr) / 2
        a, b, c =  arr[0], arr[1], arr[2]
        self.__height = (p * (p - a) * (p - b) * (p - c)) ** 0.5 / (2 * max(arr))

    def get_square(self):
        """
        возвращает площадь треугольника
        :return:
        """
        arr = super().get_sides()
        p = sum(arr) / 2
        a, b, c = arr[0], arr[1], arr[2]
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    def __init__(self, colors: tuple, *sides):
        super().__init__(colors, 12)
        if len(sides) == 1:
            arr = [sides[0]] * 12
        else:
            arr = [1] * 12
        super().set_sides(*arr)

    def get_volume(self):
        """
        Метод get_volume, возвращает объём куба.
        :return: Volume
        """
        return super().get_sides()[0] ** 3


"""
t1 = Triangle(3, 4, 5)
print(t1.get_sides())
print(t1.get_square())

k1 = Cube(4)
print(k1.get_sides())
print(k1.get_volume())

c1 = Circle(22)
print(c1.get_sides())
print(c1.get_square())

ff4 = Figure(4)
#print(ff)
ff4.set_sides(3, 4, 5, 6)
print(ff4.get_sides())

ff8 = Figure(8)
ff8.set_sides(3, 4, 5, 6, 30, 40, 50, 60)
print(ff8.get_sides())

ff.chk_clr(1, 2, 3)
ff.chk_clr(-1, 2, 3)
ff.chk_clr(1, 256, 3)
ff.chk_clr(1, 2, 3.5)

ff.set_color(0, 128, 255)
print(ff.get_color())
ff.set_color(0, 128, 256)
print(ff.get_color())

    def chk_clr(self, r, g, b):
        ss = f"colors {r} {g} {b}"
        if Figure.__is_valid_color(r, g, b):
            print(ss, '- ok')
        else:
            print(ss, '- bad')

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.__sides[0] / (2 * pi)

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, 
то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Код для проверки:
"""


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

"""
Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""
#eof-module6hard.py