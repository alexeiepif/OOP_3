#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать абстрактный базовый класс Pair
# с виртуальными арифметическими операциями.
# Реализовать производные классы Complex (комплексное число)
# и Rational (рациональное число).

from abc import ABC, abstractmethod
from math import gcd


class Pair(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def values(self):
        pass

    def __eq__(self, other):
        return self.values == other.values


class Complex(Pair):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = (
            self.real * other.real - self.imag * other.imag
        )  # Re(a * b)
        imag_part = (
            self.real * other.imag + self.imag * other.real
        )  # Im(a * b)
        return Complex(real_part, imag_part)

    # Переопределяем деление для комплексных чисел
    def __truediv__(self, other: Pair):
        denom = (
            other.real**2 + other.imag**2
        )  # Модуль другого числа в квадрате
        real_part = (
            self.real * other.real + self.imag * other.imag
        ) / denom  # Re(a / b)
        imag_part = (
            self.imag * other.real - self.real * other.imag
        ) / denom  # Im(a / b)
        return Complex(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {self.imag}i"

    @property
    def values(self):
        return self.real, self.imag


class Rational(Pair):
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ValueError("Недопустимое значение знаменателя")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Оба аргумента должны быть целыми числами!")

        self.numerator = numerator
        self.denomerator = denominator

        self.integer_number = self.denomerator == 1
        if not self.integer_number:
            self.__reduce()

    def __reduce(self):
        sign = 1
        if self.numerator * self.denomerator < 0:
            sign = -1
        a, b = abs(self.numerator), abs(self.denomerator)
        c = gcd(a, b)
        self.numerator = sign * (a // c)
        self.denomerator = b // c
        self.integer_number = self.denomerator == 1

    def __add__(self, other):
        x = (
            self.numerator * other.denomerator
            + other.numerator * self.denomerator
        )
        y = self.denomerator * other.denomerator
        r = Rational(x, y)
        r.__reduce()
        return r

    def __sub__(self, other):
        x = (
            self.numerator * other.denomerator
            - other.numerator * self.denomerator
        )
        y = self.denomerator * other.denomerator
        r = Rational(x, y)
        r.__reduce()
        return r

    def __mul__(self, other):
        x = self.numerator * other.numerator
        y = self.denomerator * other.denomerator
        r = Rational(x, y)
        r.__reduce()
        return r

    def __truediv__(self, other):
        x = self.numerator * other.denomerator
        y = self.denomerator * other.numerator
        r = Rational(x, y)
        r.__reduce()
        return r

    def __str__(self):
        if self.integer_number:
            return f"{self.numerator}"
        return f"{self.numerator} / {self.denomerator}"

    @property
    def values(self):
        return self.numerator, self.denomerator


if __name__ == "__main__":
    first_complex = Complex(2, 3)
    second_complex = Complex(4, 5)
    print(
        f"Сумма комплексных чисел {first_complex} и {
          second_complex} равна {first_complex + second_complex}"
    )
    print(
        f"Разность комплексных чисел {first_complex} и {
          second_complex} равна {first_complex - second_complex}"
    )
    print(
        f"Произведение комплексных чисел {first_complex} и {
          second_complex} равна {first_complex * second_complex}"
    )
    print(
        f"Деление комплексных чисел {first_complex} и {
          second_complex} равна {first_complex / second_complex}"
    )

    r1 = Rational(3, 4)
    r2 = Rational(5, 6)
    print(f"r1 = {r1}")
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 / r2 = {r1 / r2}")

    r3 = Rational(5, -3)
    r4 = Rational(-6, 9)
    print(f"r3 = {r3}")
    print(f"r4 = {r4}")
    print(f"r3 + r4 = {r3 + r4}")
    print(f"r3 - r4 = {r3 - r4}")
    print(f"r3 * r4 = {r3 * r4}")
    print(f"r3 / r4 = {r3 / r4}")

    r5 = r6 = Rational(8, 4)
    print(f"r5 = {r5}")
    print(f"r6 = {r6}")
    print(f"r5 + r6 = {r5 + r6}")
    print(f"r5 - r6 = {r5 - r6}")
    print(f"r5 * r6 = {r5 * r6}")
    print(f"r5 / r6 = {r5 / r6}")

    print(f"r5 == r6: {r5 == r6}")
    print(f"r5 == r2: {r5 == r2}")
