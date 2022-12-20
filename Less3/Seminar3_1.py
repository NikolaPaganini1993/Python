# 1. List comperehesion []
# my_list = [x for x in range(10)]
# print(my_list)

# import random
# my_list = [random.randint(0,10) for x in range(10)]
# print(my_list)

# import random
# def rand_letter():
#     x = random.randint(0, 10)
#     if x % 2 == 0:
#         return 'A'
#     else:
#         return 'B'
# my_list = [rand_letter() for x in range(10)]
# print(my_list)

# my_list = [x for x in range(-10, 10) if x % 2 == 0 or x > 0]
# print(my_list)

# my_list = {x for x in range(-10, 10)}
# print(my_list)
# for i in my_list:
#     print(i)


# 2. map()
# import random
# def rand_letter():
#     x = random.randint(0, 10)
#     if x % 2 == 0:
#         return '123'
#     else:
#         return '321'
# my_list = [rand_letter() for _ in range(-10, 10)]
# new_list = list(map(int, my_list))
# print(my_list)
# print(new_list)

# import random
# def rand_letter():
#     x = random.randint(0, 10)
#     if x % 2 == 0:
#         return 5
#     else:
#         return 10
# def degree(x):
#     if x % 2 == 0:
#         return x
# my_list = [rand_letter() for _ in range(-10, 10)]
# print(my_list)
# my_list = list(filter(degree, my_list))
# print(my_list)


# 3. Enumerate()
# my_list = [rand_letter() for _ in range(15)]
# print(my_list)
# for i in enumerate(my_list):
#     if i == "A":
#         print(i)


# 4. Zip
# import random
# def rand_letter():
#     x = random.randint(0, 10)
#     if x % 2 == 0:
#         return 5
#     else:
#         return 10
# first_list = [rand_letter() for _ in range(15)]
# second_list = [rand_letter() for _ in range(10)]
# third_list = [rand_letter() for _ in range(5)]
# print(first_list)
# print(second_list)
# print(third_list)
# all_list = list(zip(first_list, second_list, third_list))
# print(all_list)


# 5.Лямбда - функция
# import random
# def rand_letter():
#     x = random.randint(0, 10)
#     if x % 2 == 0:
#         return 5
#     else:
#         return 10
# def degree(x):
#     if x % 2 == 0:
#         return x
# my_list = [x for x in range(10)]
# my_list = list(map(lambda x: x > 2, my_list))
# print(my_list)
# print(type(my_list))

# Задачи:
# Задача 1.
# В файле находится N натуральных чисел,
# записанных через пробел.
# Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# with open('filenumber.txt', 'r') as file:
#     my_string = file.readline()
# my_list = list(map(int, my_string.split()))
# print(my_list)
# def find_number(sm_list: list) -> int:
#     for i in range(1, len(sm_list)):
#         if sm_list[i] - 1 != sm_list[i - 1]:
#             return sm_list[i] - 1
# out_number = find_number(my_list)
# print(out_number)

# Задача 2.
# 1. Дан список чисел. Создайте список, в который попадают
# числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3]
# или [1, 7]
# или [1, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# print(my_list)
# find = int(input('Введите стартовый элемент: '))
# index = 0
# for i, item in enumerate(my_list):
#     if item == find:
#         index = i
#         break
# def create_special_list(sm_list: list) -> list:
#     element = sm_list[0]
#     new_list = [sm_list[0]]
#     for i in range(1, len(sm_list)):
#         if sm_list[i] - 1 == element:
#             new_list.append(sm_list[i])
#             element = sm_list[i]
#     return new_list
# special_list = my_list[index:]
# print(create_special_list(special_list))

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 < b1 < a2 < b2:
    print('пустое множество')
elif a2 < b2 < a1 < b1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
else:
    print(a1, b1)











