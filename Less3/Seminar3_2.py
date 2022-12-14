# Дана последовательность чисел.
# Получить список уникальных элементов
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_list_2 = []
# for i in range(len(my_list)):
#     count = 0
#     for j in range(len(my_list)):
#         if my_list[i] == my_list[j]:
#             count += 1
#     if count == 1:
#         my_list_2.append(my_list[i])
# print(my_list)
# print(my_list_2)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_list_2 = []
# my_dict = {}
# for i in my_list:
#     my_dict[i] = my_list.count(i)
#     if my_dict.get(i) == 1:
#         my_list_2.append(i)
# print(my_dict)
# print(my_list_2)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_dict = {}
# my_list_2 = []
# for item in my_list:
#     my_dict[item] = my_dict.get(item, 0) + 1
# for key, value in my_dict.items():
#     if value == 1:
#         my_list_2.append(key)
# print(my_list)
# print(my_dict)
# print(my_list_2)

# 1.
# Напишите программу вычисления арифметического
# выражения заданного строкой.
# Используйте операции +, -, /, *.
# приоритет операций стандартный.
# Пример:
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

# my_str = '1/ 2 - 5'
# my_str = my_str.replace(' ', '')
# my_str = my_str.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
# my_list = my_str.split()
# for i in range(len(my_list)):
#     if my_list[i].isdigit():
#         my_list[i] = int(my_list[i])
# def calculate_str(sm_list: list) -> int:
#     while ('*' in sm_list) or ('/' in sm_list):
#         i = 0
#         while i < len(sm_list):
#             if sm_list[i] == '*':
#                 sm_list[i - 1] = sm_list[i - 1] * sm_list[i + 1]
#                 sm_list.remove(sm_list[i])
#                 sm_list.remove(sm_list[i])
#                 print(sm_list)
#             elif sm_list[i] == '/':
#                 sm_list[i - 1] = sm_list[i - 1] / sm_list[i + 1]
#                 sm_list.remove(sm_list[i])
#                 sm_list.remove(sm_list[i])
#             else:
#                 i += 1
#     print(sm_list)
#     while ('+' in sm_list) or ('-' in sm_list):
#         i = 0
#         while i < len(sm_list):
#             if sm_list[i] == '+':
#                 sm_list[i - 1] = sm_list[i - 1] + sm_list[i + 1]
#                 sm_list.remove(sm_list[i])
#                 sm_list.remove(sm_list[i])
#                 print(sm_list)
#             elif sm_list[i] == '-':
#                 sm_list[i - 1] = sm_list[i - 1] - sm_list[i + 1]
#                 sm_list.remove(sm_list[i])
#                 sm_list.remove(sm_list[i])
#             else:
#                 i += 1
#     print(sm_list)
#     return sm_list[0]
# answer = calculate_str(my_list)
# print(my_list)
# print(answer)

from random import randint as RI

def create_pattern(min: int, max: int) -> dict:
    degree = int(input('Введите степень максимальную многочлена: '))
    equation_pattern = {}
    for key in range(degree, -1, -1):
        value = RI(min, max)
        equation_pattern[key] = value
    return equation_pattern
print(create_pattern(- 10, 10))

def decode_equation(equation: dict) -> str:
    new_equation = ''
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'-{value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '
    return new_equation + '= 0'

