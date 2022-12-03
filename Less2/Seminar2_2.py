# c = 0
# def function():
#     global c
#     c = a + b
# print(c)

# def function():
#     new_list = []
#     for i in range(10):
#         new_list.append(i)
#     return new_list
# my_list = function()
# print(my_list)

# def function(a: int) -> list:
#     new_list = []
#     for i in range(a):
#         new_list.append(i)
#     return new_list
# print(function(3))

# def function(a: int, *arqs) -> list:
#     new_list = []
#     for i in range(a):
#         number = random.randint(arqs[0], arqs[1])
#         new_list.append(number)
#     return new_list
# print(function(4, 0, 100))

# def function(a: int = 10, b: int = 100) -> list:
#     new_list = []
#     for i in range(a):
#         number = random.randint(0, b)
#         new_list.append(number)
#     return new_list
# print(function())

#
# import random
# def function(a: int = 10, b: int = 100, c: int = 0) -> list:
#     new_list = []
#     for i in range(a):
#         number = random.randint(c, b)
#         new_list.append(number)
#     return new_list
# print(function(4, 5, 3))

# import random
# def input_int(text: str, error: str) -> int:
#     while True:
#         try:
#             number = int(input(text))
#             return number
#         except:
#             print(error)



             #множество


# СПИСКИ
# my_list = [1, 2, 3, 4, 1, 3]             #список
# my_list[0] = 'a'
# print(my_list)

# КОРТЕЖ
# my_tuple = (234, 456, 662)            #кортеж
# print(my_tuple[2])
# my_tuple = list(my_tuple)
# my_tuple[2] = 'f'
# print(my_tuple)
# my_tuple = tuple(my_tuple)
# print(my_tuple)

# МНОЖЕСТВА
# my_set = {'квадрат', 'круг', 'треугольник'}
# print(my_list)
# my_list = set(my_list)
# my_list = list(my_list)
# print(my_list)
# print(my_set)
# my_set.add('прямоугольник')
# print(my_set)
# my_set.add('2')
# print(my_set)
# my_set.add((2, 2))
# print(my_set)
# figure = 'прямоугольник'
# if figure in my_set:
#     print(True)
# else:
#     print(False)

# СЛОВАРЬ
# my_dict = {1:'one', 2:'two', 3:'three'} #словарь
# print(my_dict.get(2))
# for i in my_dict:
#     print(i)
# for key, value in my_dict.items():
#     print(key)
#     print(value)

# 1.Задайте строку из набора чисел.
#   Напишите программу, которая покажет
#   большее и меньшее число.
#   В качестве символа-разделителя используйте пробел.

# my_list = input('Введите числа через пробел: ').split(' ')
# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])
# print(min(my_list))
# print(max(my_list))

# 1.Задайте два числа.
#   Напишите программу,
#   которая найдёт НОК
#   (наименьшее общее кратное)
#   этих двух чисел.

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# for i in range(1, a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# if a > b:
#     c = a
# else:
#     c = b
# while c <= a * b:
#     if c % a == 0 and c % b == 0:
#         print(c)
#         break
#     c += 1

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# i = 1
# while(max(a, b) * i) % min(a, b) != 0:
#     i += 1
# print(max(a, b) * i)

