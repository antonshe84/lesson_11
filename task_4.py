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
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    count_units = 0
    count_type = 0
    name_count = {}
    sum_numb = 0
    type = "принтер"

    def __init__(self, name, price):
        self.name = name
        print(f"Добавлен {self.type} {self.name}")
        if OfficeEquipment.is_valid(price):
            self._price = int(price)
        else:
            print("Цена указана неверно")
            self._price = 0
        self.sum_numb = 0
        OfficeEquipment.name_count[self.name] = 0
        OfficeEquipment.count_type += 1

    @property
    def add_one(self):
        self.sum_numb += 1
        OfficeEquipment.count_units += 1
        OfficeEquipment.name_count[self.name] += 1
        print("Добавлена 1 единица")

    @staticmethod
    def is_valid(s):
        if str(s).isdigit():
            return True
        else:
            return False

    @classmethod
    def get_count_type(cls):
        return cls.count_type

    @classmethod
    def get_count_units(cls):
        return cls.count_units

    @classmethod
    def get_list_type(cls):
        return cls.name_count

    def add_several(self, number):
        if OfficeEquipment.is_valid(number):
            self.sum_numb += int(number)
            OfficeEquipment.count_units += int(number)
            OfficeEquipment.name_count[self.name] += int(number)
            print(f"Добавлено {number} единиц")
        else:
            print("Введены некорректные данные")

    def moving(self, number, subdivision):
        if number <= self.sum_numb:
            self.sum_numb -= number
            OfficeEquipment.count_units -= number
            OfficeEquipment.name_count[self.name] -= int(number)
            print(f"Перемщено {number} единиц в подраздедение {subdivision}. Остаток на складе: {self.sum_numb}\n")
        else:
            print(f"На складе доступно только {self.sum_numb} единиц, невозможно переместить\n")


class Printer(OfficeEquipment):
    def __init__(self, name, price, color):
        self.type = "принтер"
        self.color = color
        super().__init__(name, price)

    def __str__(self):
        return f"\n- Наименование: {self.name}\n  Цена: {self._price}$\n  Цвет: " \
               f"{self.color}\n  Колличество на складе: {self.sum_numb}\n"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, dpi):
        self.dpi = dpi
        self.type = "сканер"
        super().__init__(name, price)

    def __str__(self):
        return f"\n- Наименование: {self.name}\n  Цена: {self._price}$\n  Разрешение: " \
               f"{self.dpi}dpi\n  Колличество на складе: {self.sum_numb}\n"


class Copier(OfficeEquipment):
    def __init__(self, name, price, placing):
        self.placing = placing
        self.type = "ксерокс"
        super().__init__(name, price)

    def __str__(self):
        return f"\n- Наименование: {self.name}\n  Цена: {self._price}$\n  Размещение: " \
               f"{self.placing}\n  Колличество на складе: {self.sum_numb}\n"


sklad_1 = OfficeEquipmentWarehouse("Цех 1")
sklad_2 = OfficeEquipmentWarehouse("Цех 3")

p1 = Printer("Canon I20", 100, "black")
p1.add_one
p1.add_several(10)
print(p1)

p1.moving(20, sklad_1.name)

s1 = Scanner("HP S20", 120, 2400)
s1.add_one
s1.add_one
s1.add_several("gg")
s1.add_several("8")
s1.add_several(7)
print(s1)
s1.moving(15, sklad_2.name)

c1 = Copier("Xerox X20", "hhf", "top")
c1.add_one
c1.add_several(50)
print(c1)

c2 = Copier("Xerox XС20", "200", "top")

print()
print(f"Всего моделей оргтехники: {OfficeEquipment.get_count_type()}")
print(f"Список моделей и их количество: {OfficeEquipment.get_list_type()}")
print(f"Общее количество единиц на складе: {OfficeEquipment.get_count_units()}")
