#1 задание
#Напишите функцию make_sentence, которая принимает один именованный аргумент words,
# который должен быть списком строк, и возвращает строку, составленную из элементов списка, разделенных пробелами и
#заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию используется список ["This", "is", "a", "sentence"].

def make_sentence(words=("This", "is", "a", "sentence")):
    return" ".join(words) + "."
print(make_sentence(['Hi', 'my', 'dear']))


#2 Напишите функцию sum_of_squares, которая принимает произвольное количество позиционных аргументов,
# которые должны быть числами, и возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.
def sum_of_squares(*numbers: int | float) -> int | float:
    sum_squares = 0
    for number in numbers:
        sum_squares += number**2
    return sum_squares
print(sum_of_squares(2,6,5,8,9))

#3 Напишите функцию greet, которая принимает два именованных аргумента: name и language.
# Аргумент name должен быть строкой, а аргумент language должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".

def greet(name="", language="en"):
    if language == "ru":
        return f"Привет, {name}!"
    elif language == "fr":
        return f"Bonjour, {name}!"
    return f"Hello, {name}!"
print(greet(name="Anna", language="ru"))

#4 - тут не получается

# Напишите функцию print_info, которая принимает произвольное количество именованных аргументов (**kwargs) и выводит их в формате
#"key: value" по одной паре на строку. Напоминаю, что kwargs в функции будет словарем.
# Если функции не передано ни одного аргумента, она должна вывести "No info given.".
#Пример вызова: print_info(name="Alex", age=25, city="Amsterdam")

def print_info(**kwargs):
    if not kwargs:
        print("No info given.")
        return

    for key, value in kwargs.items():
        print (f"{key}:{value}")

print(print_info(name="Alex", age=25, city="Amsterdam"))

# 5 Тут не получается ((
#
# Напишите функцию print_table, которая принимает произвольное количество именованных аргументов в виде пар ключ-значение
# и выводит их в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не передано ни одного аргумента,
# она должна вывести "No data given."
# Пример вызова: print_table(name="Bob", age=30, city="Amsterdam")

def print_table(**kwargs):
    if not kwargs:
        print("No data given.")

    for key, value in kwargs:
        print (f""
               | Key | Value    |
               |-----|----------|
               |f"{key}:7|{value}:18")""
print(print_table(name="Bob", age=30, city="Amsterdam"))

#6  - не понимаю, как проделать операцию над числами с помощью этого {operation}, куда его засунуть ((((

# Напишите функцию calculate, которая принимает произвольное количество позиционных аргументов,
# которые должны быть числами, и один именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/". Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи. Если функции не передано ни одного позиционного аргумента, она должна
#вернуть 0.Если аргумент operation не указан, то по умолчанию используется "+".
#Пример вызова: calculate(1, 2, 3, operation="*")

def calculate(*args, operation='+'):
    res = 0
    for numbers in args:
        res += int(numbers)
    return res
print(calculate(1, 2, 4, operation="*"))

#7 тут на занятии пояснили, так бы не решила сама ...
#
# Напишите функцию print_triangle, которая принимает один именованный аргумент height, который должен быть положительным целым числом,
# и выводит равнобедренный треугольник из символов "*" с заданной высотой. Если аргумент height не указан, то по
# умолчанию используется число 5. Пример вызова: print_triangle(height=4)

def print_triangle(height=5):
    i = 0
    while i <= height:
        line = "*"*(i + (i-1))
        print(f"{line:^10}")
        i += 1

print_triangle(4)

#8 Напишите функцию create_post, которая создает пост для блога, основываясь на переданных параметрах.
# Обязательными параметрами являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет текущая значение “general”.
# Функция должна возвращать словарь поста

def create_post(title: str, text: str, author: str, cathegory="general", **kwargs):
    post = {
        "title": title,
        "text": text,
        "author": author,
        "cathegory": cathegory,
    }
    return post
print(create_post('Alena', 'атмоваитовб', 'Brown'))

#9 Напишите функцию create_product, которая создает товар для интернет-магазина, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, цена и категория. Необязательным параметром является рейтинг.
# Если он не был передан параметр, то по умолчанию будет 0. Функция должна возвращать словарь товара.

def create_product(name:  str, price: int, cathegory: str, rate=0, *args):
    product = {
        "name": name,
        "price": price,
        "cathegory": cathegory,
        "rate": rate,
    }
    return product
print(create_product('Mouse', 12, 'Cheap'))

#10 - не получилось вывести  - ругается, что не все ввела

# Напишите функцию create_student, которая создает словарь студента для учебного заведения,
# основываясь на переданных параметрах. Обязательными параметрами являются: имя, фамилия, отчество и группа.
#Также дополнительными параметрами могут быть: дата поступления в виде строки «19.10.2023», средний бал, семестр обучения,
# номер телефона, адрес. Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть в словаре

def create_student(first_name: str, last_name: str, surname: str, group: int, **kwargs):
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "surname": surname,
        "group": group,
    }
    student.update(kwargs)
    return student

student1 = create_student(
    "user17018",
    "password2",
    "Alex",
    23,
    email="example@mail.com",
    phone="1i9239172837",
)
print(student1)

# или вот так:

def create_student(first_name: str, last_name: str, surname: str, group: int, **kwargs):
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "surname": surname,
        "group": group,
    }
    student.update(kwargs)
    return student

def create_student_new(notification_text: str, **kwargs):
    new_student = create_student(**kwargs)
    return new_student

notification_text = "Создание пользователя"
student1 = create_student_new(
    notification_text,
    email="example@mail.com",
    phone="1i9239172837",
)
print(create_student_new(student1))
