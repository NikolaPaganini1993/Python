# a = 123
# b = 1.23
# c = 'Hello World!!!'
# print(a, b, c)
# print(a, '-',b, '-',c)
# print('{} - {} - {}'.format(a, b, c))
# print('{1} - {2} - {0}'.format(a, b, c))
# print(f'{a} - {b} - {c}')

# f = True
# z = False
# print(f, z)

# list = [1, 2, 3]
# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# print('Введите a')
# a = input()
# print('Введите b')
# b = input()
# print(a, '+', b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a + b)

# a = 5
# b = 2
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# g = a // b
# h = a % b
# i = a ** b
# print(c, d, e, f, g, h, i)

# a#  = 1.3123
# b = 3
# c = round(a * b, 3)
# print(c)

# a = 3
# a += 5
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwerty1'
# b = 'qwerty'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# a = 3
# b = 5
# print(func<a>b)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# f = [1, 2, 3, 4]
# is_odd = not f[1] % 2
# print(is_odd)

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же Маша!')
# else:
#     print('Привет,',username)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Это же МАРИНААА!')
# elif username == 'Коля':
#     print('Здравствуй, хазяин!')
# else:
#     print('Привет,',username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# r = range(2, 10, 2)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# text = 'съешь еще этих мягих французских булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))
# print(text[0])
# print(text[1])
# print(text[len(text)-1])
# print(text[-2])
# print(text[:])
# print(text[:2])
# print(text[2:5])

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers = list(range(1, 6))
# print(numbers)
# ran = range(1, 6)
# numbers[0] = 10
# print(len(numbers))
# print(numbers)
# for i in numbers:
#     i*=2
#     print(i)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# colors =['Red', 'Green', 'Blue']
# for e in colors:
#     print(e) # Red Green Blue
# for e in colors:
#     print(e*2) # RedRed GreenGreen BlueBlue
# colors.append('Gray')
# print(colors == ['Red', 'Green', 'Blue', 'Gray'])
# print(colors)
# colors.remove('Red')
# print(colors)
# del colors[0]
# print(colors)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))



