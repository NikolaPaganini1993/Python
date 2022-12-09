# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
#    сумму элементов списка, стоящих на нечётной позиции.
#    Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# size = int(input('Введите размер списка: '))
# my_list = [random.randint(-10, 10) for _ in range(size)]
# print(my_list)
# summa = 0
# for i in range(1, len(my_list), 2):
#     summa += my_list[i]
# print(summa)

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

# import random
# size = int(input('Введите размер списка: '))
# my_list =[random.randint(-10, 10) for _ in range(size)]
# print(my_list)
# if len(my_list) % 2 == 0:
#     center = int(len(my_list) / 2)
# else:
#     center = int(len(my_list) / 2) + 1
# new_list = []
# for i in range(center):
#     new_list.append(my_list[i] * my_list[-i])
# print(new_list)

# text = input("Введите список чисел, разделенных пробелом: ").split()
# my_list = list(map(int, text))
# print(my_list)
# new_list = []
# for i in range(len(my_list) // 2):
#     mult = my_list[i] * my_list[len(my_list) - i - 1]
#     new_list.append(mult)
# print(new_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#    и минимальным значением дробной части элементов. (подробности в конце записи семинара).
#    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# size = int(input('Введите размер списка: '))
# my_list =[round(random.uniform(0, 10), 2) for _ in range(size)]
# print(my_list)
# def devine(number: float) -> float:
#     return round(number - int(number), 2)
# my_list = list(map(devine, my_list))
# print(max(my_list) - min(my_list))

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

# number = int(input('Введите число в десятичной системе: '))
# bi_number = ''
# while number > 0:
#     bi_number = str(number % 2) + bi_number
#     number //= 2
# print(bi_number)

# number = int(input('Введите число: '))
# answer = ''
# while number > 0:
#     answer = str(number % 2) + answer
#     number = number // 2
# print(answer)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
#    Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# size = int(input('Введите размер последовательности: '))
# fibo = [1, 0, 1]
# for i in range(3, size + 3):
#     fibo.append(fibo[i - 2] + fibo[i - 1])
# for i in range(size):
#     fibo.insert(0, fibo[1] - fibo[0])
# print(fibo)

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


