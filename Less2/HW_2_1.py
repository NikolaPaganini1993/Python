# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
#    сумму элементов списка, стоящих на нечётной позиции.
#    Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# my_list = []
# for i in range(5):
#     my_list.append(randint(-10, 10))
# print(my_list)
# summa = 0
# count = 1
# while count < len(my_list):
#     summa = summa + my_list[count]
#     count = count + 2
# print(summa)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#    [2, 3, 4, 5, 6] => [12, 15, 16]
#    [2, 3, 5, 6] => [12, 15]

text = input("Введите список чисел, разделенных пробелом: ").split()
my_list = list(map(int, text))
print(my_list)
new_list = []
for i in range(len(my_list) // 2):
    mult = my_list[i] * my_list[len(my_list) - i - 1]
    new_list.append(mult)
print(new_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#    и минимальным значением дробной части элементов. (подробности в конце записи семинара).
#    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# my_list = []
# for i in range(5):
#     my_list.append(round(random.uniform(0, 10), 2))
# print(my_list)
# for i in range(len(my_list)):
#     if my_list[i] != 0:
#         my_list[i] = my_list[i] - int(my_list[i])
# for i in range(len(my_list)):
#     my_list[i] = round(my_list[i], 2)
# answer = round(max(my_list) - min(my_list), 2)
# print(answer)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без применения встроеных методов (арифметически)
#    Пример:
#    45 -> 101101
#    3 -> 11
#    2 -> 10

# number = int(input('Введите число: '))
# answer = ''
# while number > 0:
#     answer = str(number % 2) + answer
#     number = number // 2
# print(answer)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
#    Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# number = int(input('Введите число: '))
# my_list = [-1, 1, 0, 1, 1]
# fib1 = 1
# fib2 = 1
# fib3 = 1
# fib4 = -1
# for i in range(2, number):
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     my_list.append(fib2)
# for i in range(2, number):
#     fib_sum2 = fib3 - fib4
#     fib3 = fib4
#     fib4 = fib_sum2
#     my_list.insert(0, fib4)
# print(my_list)