"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipmentWarehouse:
    def __init__(self, address):
        self.address = address


class OfficeEquipment:
    sum_numb = 0
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.sum_numb = 0

    @property
    def add_one(self):
        self.sum_numb += 1
        print("Добавлена одна единица")

    def add_several(self, number):
        self.sum_numb += number
        print(f"Добавлено {number} единиц")

    def moving(self, number, subdivision):
        if number <= self.sum_numb:
            self.sum_numb -= number
            print(f"Перемщено {number} единиц в подраздедение {subdivision}. Остаток на складе: {self.sum_numb}\n")
        else:
            print(f"На складе доступно только {self.sum_numb} единиц, невозможно переместить\n")

class Printer(OfficeEquipment):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def __str__(self):
        return f"Наименование: {self.name}\nЦена: {self._price}$\nЦвет: " \
               f"{self.color}\nКолличество на складе: {self.sum_numb}\n"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, dpi):
        super().__init__(name, price)
        self.dpi = dpi

    def __str__(self):
        return f"Наименование: {self.name}\nЦена: {self._price}$\nРазрешение: " \
               f"{self.dpi}dpi\nКолличество на складе: {self.sum_numb}\n"


class Copier(OfficeEquipment):
    def __init__(self, name, price, placing):
        super().__init__(name, price)
        self.placing = placing

    def __str__(self):
        return f"Наименование: {self.name}\nЦена: {self._price}$\nРазмещение: " \
               f"{self.placing}\nКолличество на складе: {self.sum_numb}\n"



p1 = Printer("Canon I20", 100, "black")
p1.add_one
p1.add_several(10)
print(p1)

p1.moving(5, "Цех №1")



s1 = Scanner("HP S20", 120, 2400)
s1.add_one
s1.add_one
s1.add_several(7)
print(s1)
s1.moving(15, "Цех №6")


c1 = Copier("Xerox X20", 150, "top")
c1.add_one
c1.add_several(50)
print(c1)



