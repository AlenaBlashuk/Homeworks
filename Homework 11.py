# 1
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому # лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, add1: str = ""):
        self.add1 = add1

    def show_my_drink(self) -> None:
        if self.add1 != "":
            print(f"Газировка и {self.add1}")
        else:
            print(f"Обычная газировка")

a = Soda()
print(a.show_my_drink())

#2 Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого необходимо создать класс TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#– Ура, можно построить треугольник!;
#– С отрицательными числами ничего не выйдет!;
#– Нужно вводить только числа!;
#– Жаль, но из этого треугольник не сделать

class TriangleChecker:
    def __init__(self, side1: int, side2: int, side3: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self) -> None:
        if sum(self.side1, self.side2) > self.side3 and sum(self.side1, self.side3) > self.side2 and sum(self.side2, self.side3) > self.side1:
            print(f"Ура, можно построить треугольник!")
            else:
            print(f"Жаль, но из этого треугольник не сделать")
        elif self.side1 <= 0:
            print(f"С отрицательными числами ничего не выйдет!")
        elif self.side2 <= 0:
            print(f"С отрицательными числами ничего не выйдет!")
        elif self.side3 <= 0:
            print(f"С отрицательными числами ничего не выйдет!")
        # вот тут тоже для каждлого нужно прописать условие isinstance?
        elif isinstance(self.side1, (int | float)):
            print(f"Нужно вводить только числа!")

    def __str__(self) -> str:
        return f"{}" # не поняла, что тут вводить надо)

g = TriangleChecker(1,2,3)
print(g.is_triangle())

#3 Необходимо создать класс KgToPounds, в который принимает количество килограмм, а с помощью метода to_pounds()
# они переводятся в фунты. Необходимо закрыть доступ к переменной kg. Также, реализовать методы:
#- set_kg() - для задания нового значения килограммов (записывать только числовые значения),
#- get_kg() - для вывода текущего значения кг.
#Во второй версии необходимо использовать декоратор property для создания setter и getter взамен set_kg и get_kg

class KgToPounds:

    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pounds(self) -> int | float:
        return self.__kg*0.14

    @property
    def get_kg(self):
        return self.__kg

    @kg.setter
    def set_kg(self, kg: int):
        self.__kg = kg

    def __str__(self):
        return self.__kg

er = KgToPounds(12)
print(er.to_pounds())
KgToPounds = 5
print(KgToPounds.to_pounds())

#4 Строки в Питоне сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что больше: Apple или Яблоко,
# – то Яблоко окажется бОльшим. А все потому, что английская буква A имеет значение 65 (берется из таблицы кодировки),
# а русская буква Я – 1071. Надо создать новый класс RealString, который будет принимать строку и сравнивать по количеству
#входящих в них символов. Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString

class RealString:

    def __init__(self, stroke: str):
        self.stroke = stroke

# как узнать сумму значений букв - как обратиться к кодировке? вызвать нужно UTF 8 и посчитать сумму у каждой буквы
    def __ge__(self, other) -> int:
        return f"len{self.stroke}))"

# 5 Напишите класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса Rectangle в формате “Прямоугольник с шириной width и высотой height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является квадратом, и False в противном случае.
# Этот метод должен быть декорирован как property.

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return self.width*2 + self.height*2

    @property # тут ошибка выдает: TypeError: 'NoneType' object is not callable
    def is_square(self) -> bool:
        if self.width == self.height:
            return True


a = Rectangle(5,6)
print(a.get_area())
print(a.get_perimeter())
print(a.is_square())

# 6 Напишите класс Person, который имеет атрибуты name (имя), age (возраст) и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и устанавливает значение атрибута name равным new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше или равен 18,
# и False в противном случае. Этот метод должен быть декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и создает и возвращает объект класса Person
# на основе строки s. Строка s должна иметь формат “name-age-gender”, где name - имя, age - возраст и gender - пол. Этот
# метод должен быть декорирован как classmethod

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.__name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        self.__name = name

    @property
    def set_name(self, new_name: str):
        self.__name = new_name

    @staticmethod
    def is_adult(age: int) -> bool:
        if age >= 18:
            return True

    @classmethod
    def create_from_string(cls, s: str):
        s.split()
        return cls(s[0], s[1], s[2])

p = Person('Alya', 12, 'women')
print(p.age)
p1 = Person.create_from_string(Person, 'Alya-12-women')
print(Person.create_from_string)