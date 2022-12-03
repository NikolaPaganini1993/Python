# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр.
#    Пример:
#    6782 -> 23
#    0,56 -> 11
import random

# number = float(input('Введите вещественное число N: '))
# a = int(number)
# print('Целая часть числа N = ', a)
# b = number - int(number)
# c = round(b, 2)
# print('Дробная часть числа N = ', c)
# summa = 0
# while a != 0:
#     digit = a % 10
#     summa = summa + digit
#     a = a // 10
# while c != 0:
#     digit = int(c * 10)
#     summa = summa + digit
#     c = c * 10 - int(c * 10)
# print('Сумма = ', summa)

# number = input('Введите число: ')
# summa = 0
# for i in number:
#     if i.isdigit(): #isdigit() проверяет цифра ли наш элемент
#         summa += int(i)
# print(summa)

# from decimal import Decimal
# number = Decimal(input('Введите число: '))
# original = number
# def sum_digits(number: int):
#     summa = 0
#     while number > 0:
#         summa += number % 10
#         number //= 10
#     return summa
# while (number != int(number)):
#     number *= 10
# summa = sum_digits(number)
# print(f'Сумма цифр в числе {original} равна {int(sum_digits(number))}')

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
#    Вывести в консоль сам список и сумму его элементов.

# n = int(input('Введите число N: '))
#
# summa = 0
# for i in range(1, n+1):
#     my_list.append(f'{i}:{(1+1/i) ** i}')
#     summa = summa + ((1+1/i) ** i)
# print(my_list)
# print(summa)

# n = int(input('Введите число N: '))
# my_list = []
# for i in range(1, n + 1):
#     my_list.append(round(((1 + 1 / i) ** i), 2))
# print(my_list)
# print(sum(my_list))


# 3. Реализуйте алгоритм перемешивания списка.
#    Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)

# my_list = [1, 2, 3, 4, 5, 6]
# for i in range(len(my_list)):
#     n = random.randint(0, (len(my_list) - 1))
#     my_l
# 4. Написать программу, которая состоит 4 из этапов:
#    - создает список из рандомных четырехзначных чисел
#    - принимает с консоли цифру и удаляет ее из всех элементов списка
#    - цифры каждого элемента суммирует пока результат не станет однозначным числом
#    - из финального списка убирает все дублирующиеся элементы
#    - после каждого этапа выводить результат в консоль
#    Пример:
#    - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
#    - 2 этап: Введите цифру: 3
#    - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
#    - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
#    - 3 этап: [3, 1, 5, 5, 3, 5, 4]
#    - 4 этап: [3, 1, 5, 4]

# import random
# list = []
# list = random.sample(range(1000, 9999), 5)
# print(list)
# sum(list)
# print(sum(list))

# 5. Написать программу, которая будет ввыводит в консоль заданный текст
#    (Python - один из самых популярных языков программирования в мире),
#    затем принимать из консоли шаблон подстроки
#    и удалять в задданом тексте все слова в которых присутствует введенный шаблон
#    Пример:
#    Python - один из самых популярных языков программирования в мире
#    Введите подстроку: ам
#    Python - один из популярных языков в мире

# text1 = 'Python - один из самых популярных языков программирования в мире'
# print(text1)
# text2 = text1.split()
# string = input('Введите подстроку:')
# text2.remove(string)
# print(' '.join(text2))


# text1 = 'Python - один из самых популярных языков программирования в мире'
# print(text1)
# string = input('Введите подстроку:')
# print(text1.replace(string, ''))

