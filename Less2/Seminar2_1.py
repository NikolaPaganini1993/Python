# 1. Задайте список. Напишите программу,
#    которая определит, присутствует ли в заданном
#    списке строк некое число.


# list = ['asa12122', '2345asn44d', 'f349998cd']
# number = input('Введите искомое число: ')
# trigger = True
# for item in list:
#     for char in item:
#         if char == number:
#             print(f'Число {number} есть в строке {item}')
#             trigger = False
#             break
# if trigger:
#     print(f'Числа {number} нет в заданном списке')

# 3. Напишите программу, которая определит позицию
#    второго вхождения строки в списке либо сообщит, что её нет.
#    Пример:
#  - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#  - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#  - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#  - список: ["123", "234", 123, "567"], ищем: "123", ответ: False
#  - список: [], ищем: "123", ответ: False

# list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# find = input('Введите текст: ')
# count = 0
# for i in range(len(list)):
#     if list[i] == find:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(False)

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
string = "qwe"
count = 0
for i in range(len(list)):
    if list[i] == string:
        count += 1
        if count == 2:
            print(f'Второе вхождение элемента {string} на позиции {i}')
            break
else:
    print('Вхождение подстроки - нет')