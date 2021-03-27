"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class ZeroDivisionWarning(Exception):
    def __init__(self, msg):
        self.msg = msg


d1 = input("Введите первое число: ")
d2 = input("Введите второе число: ")

try:
    d1 = int(d1)
    d2 = int(d2)
    if d2 == 0:
        raise ZeroDivisionWarning("Деление на 0 не допустимо!")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionWarning as err:
    print(err)
else:
    print(f"Результат деления {d1 / d2: 0.2f}")
