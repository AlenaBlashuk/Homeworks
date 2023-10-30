#1 Напишите код, который принимает список чисел и возвращает новый список, содержащий только четные числа
# из исходного списка. Используйте функцию filter и лямбда-выражение.

numbers1 = [2, 5, 6, 5, -5, -8, 1, -9]
new_numbers = list(filter(lambda x: x > 0, numbers1))
print(new_numbers)

#2 Напишите код, который принимает список кортежей вида (имя, возраст) и возвращает новый список,
# отсортированный по возрастанию возраста. Используйте функцию sorted и ключ сортировки

persons = [('Alena', 25), ('Max', 9), ('Alex', 12)]
new_persons = list(sorted(persons, key=int(map(persons[1]))))
print(new_persons)

#3 Напишите код, который принимает список строк и возвращает новый список, содержащий только те строки,
# которые начинаются с гласной буквы. (Да да, снова эти гласные) Используйте функцию filter и множество.

list1 = ['hello', 'my', 'world', 'again']
new_list = []
a = filter(list1[0] in {аеёиоуэюя}, list1)
new_list.append(a)
print(new_list)

#или

list1 = ['hello', 'my', 'world', 'again']
new_list = list(filter(list1[x][0] in 'аеёиоуыэюя', list1))
print(new_list)

#4 Напишите код, который принимает список чисел и возвращает новый список, содержащий квадраты этих чисел.
# Используйте функцию map и lambda.

numbers = [5, 2, -3, 5, 1]
new_numbers = list(map(lambda x: x**2, numbers))
print(new_numbers)

#5 Напишите код, который принимает список слов и возвращает новый список, отсортированный по убыванию длины слов.
# Используйте функцию sorted и обратный порядок сортировки

words = ['Welcome', 'to', 'Malta']
words1 = str(words)
words1.split()
new_words = list(" ". join(sorted(words1, len(words1), reverse=True)))
print(new_words)

#6 Напишите код, который принимает строку и возвращает список, содержащий только те буквы, которые встречаются
# в слове “python”. Используйте функцию filter и оператор in.

string = 'Hello, Malta!'
new_string = list(filter(letter in 'Python', string.split()))
print(new_string)

#7 Напишите код, который принимает список чисел и возвращает новый список, содержащий эти же числа,
# умноженные на 10. Используйте функцию.


def x10(l: list):
    new_numbers = []
    for number in l:
        a = int(number)*10
        new_numbers.append(a)
    return new_numbers

all = [5, 7, 10, 12, 15]
print(x10(all))

#8 - тут не поняда, почему он на буквы разбил, а не на слова ((

# Напишите код, который принимает список слов и возвращает новый список, отсортированный по алфавиту.
# Используйте функцию sorted.

words = ['Hello', 'Malta', 'so', 'cool', 'to', 'be', 'here']
updated_words = list(" ".join(sorted(str(words))))
print(updated_words)

#9 тут не понимаю, как список в строку перевести и сразу это записать

# Напишите функцию, которая принимает список строк и возвращает новый список,
# содержащий только те строки, которые являются палиндромами. Палиндром — это слово,
# которое читается одинаково слева направо и справа налево. Используйте функцию filter и сравнение строк.

def palindrom(words: list) -> list:
    s = str(words).split()
    new_list = []
    for w in s:
        if w == reverse(w):
            new_list.append(w)
    return new_list

words = ['кот', 'тик', 'шалаш', 'пикник']
pal_words = list(filter(palindrom(words), words))
print(pal_words)
