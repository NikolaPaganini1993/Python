# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('Введите текст: ').split(' ')
# fragment = input('Введите фрагмент слова, которое  нужно будет удалить: ')
# my_list = list(text)
# new_text = []
# for i in range(len(my_list)):
#     if fragment not in my_list[i]:
#         new_text.append(my_list[i])
# print(' '.join(new_text))

# 2. Создайте программу для игры с конфетами человек против человека.
#    Условие задачи: На столе лежит 2021 конфета.
#    Играют два игрока делая ход друг после друга.
#    Первый ход определяется жеребьёвкой.
#    За один ход можно забрать не более чем 28 конфет.
#    Все конфеты оппонента достаются сделавшему последний ход.
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""


# from random import randint
#
#
# def step(name):
#     x = int(input(f"{name.title()}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name.title()}, введите корректное количество конфет: "))
#     return x
#
#
# def step_print(name, one_step, value):
#     print(f"Ходил {name.title()}, он взял {one_step}. Осталось на столе {value} конфет.")
#
#
# def bot_calc(value):
#     one_step = randint(1, 29)
#     while value - one_step <= 28 and value > 29:
#         one_step = randint(1, 29)
#     return one_step
#
# choice = input('Приветсвую, игрок, играть будешь с ботом или человеком? \n'
#                '(если хотите с человеком, введите: Человек) ')
# if choice == 'Человек':
#     player1 = input('Игрок 1, введите своё имя: ')
#     print(f'{player1.title()} готов к бою!!!')
#     player2 = input('Игрок 2, введите своё имя: ')
#     print(f'{player2.title()} готов к бою!!!')
# else:
#     player1 = input('Игрок 1, введите своё имя: ')
#     print(f'{player1.title()} готов к бою!!!')
#     player2 = 'Bot'
#     print('Bot готов к бою!!!')
#
#
# all_candy = int(input("Введите количество конфет на столе: "))
#
#
# print('Первый ход определяется жеребьёвкой')
# print(f'Если выпадет 1, то ходит {player1.title()}.')
# print(f'Если выпадет 2, то ходит {player2.title()}.')
# flag = randint(1, 2)
# print(f'Выпало: {flag}')
#
# if flag == 1:
#     print(f'Первым ходит {player1.title()}.')
# else:
#     print(f'Первым ходит {player2.title()}.')
#
# if player2 == 'Bot':
#     while all_candy > 28:
#         if flag == 1:
#             one_step = step(player1)
#             all_candy -= one_step
#             flag = False
#             step_print(player1, one_step, all_candy)
#         else:
#             one_step = bot_calc(all_candy)
#             all_candy -= one_step
#             flag = True
#             step_print(player2, one_step, all_candy)
# else:
#     while all_candy > 28:
#         if flag == 1:
#             one_step = step(player1)
#             all_candy -= one_step
#             flag = False
#             step_print(player1, one_step, all_candy)
#         else:
#             one_step = step(player2)
#             all_candy -= one_step
#             flag = True
#             step_print(player2, one_step, all_candy)
#
#
# if flag:
#     print(f"Выиграл {player1.title()}, поздравляю!!!")
# else:
#     print(f"Выиграл {player2.title()}, поздравляю!!!")


# 3. Создайте программу для игры в ""Крестики-нолики"".
#    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.