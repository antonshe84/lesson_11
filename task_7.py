"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        sign = '+' if self.b > 0 else '-'
        return f"{self.a} {sign} {abs(self.b)}i"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    # (a + bi)*(c + di) = ac + bdi + adi + bdi^2
    # где i^2 =  -1
    def __mul__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return Complex(a * c + (-1) * b * d, b * c + a * d)


c1 = Complex(4, 3)
c2 = Complex(5, 6)
print(f"c1: {c1}, c2: {c2}")
print(f"Сумма: {c1 + c2}")
print(f"Разность: {c1 - c2}")
c3 = c1 * c2
print(f"Произведение: {c3}")
print(type(c3))
