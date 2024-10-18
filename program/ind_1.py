#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Pair (пара чисел); определить методы
# изменения полей и вычисления произведения чисел.
# Определить производный класс RightAngled с полями-катетами.
# Определить методы вычисления гипотенузы и площади треугольника.


from math import sqrt


class Pair:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class RightAngled(Pair):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    @property
    def hypotenuse(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def area(self):
        return self.multiply() / 2


if __name__ == "__main__":
    pair = Pair(2, 3)
    print(f"Произведение чисел {pair} равно {pair.multiply()}")

    first_triangle = RightAngled(3, 4)
    print(
        "Гипотенуза треугольника с катетами "
        f"{first_triangle} равна {first_triangle.hypotenuse}"
    )
    print(
        "Площадь треугольника с катетами "
        f"{first_triangle} равна {first_triangle.area}"
    )
