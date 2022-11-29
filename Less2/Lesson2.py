# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('Line 12\n')
# data.write('Line 13\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('Line 111\n')
#     data.write('Line 222\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import __main__
# print(__main__.f(1))

# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string(4)) # 12

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))
# print(concatenatio(1, 2, 3, 4))

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4))

# def fib(n):                        #описали функцию, название функции и аргумент
#     if n in [1, 2]:                #если n находится в списке от 1 до 2
#         return 1                   #возвращаем единицу
#     else:                          #иначе
#         return fib(n-1) + fib(n-2) #возвращаем рекурсивный вызов для (n-1) и (n-2)
# list = []                          #создаём список
# for e in range(1, 10):             #обозначаем отрезок где будем смотреть функцию
#     list.append(fib(e))            #добавляем число
# print(list)                        #выводим результат

# a = (3, 4, 1, 21)
# print(a)
# print(a[0])
# print(a[-1])

# t = tuple(['red', 'green', 'blue'])
# print(t[0])
# print(t[2])
# print(t[-2])
# for e in t:
#     print(e)

# a = (3, 4, 1, 21)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# dictionary = {}
# dictionary = \
#     {
#         'up': 'верх',
#         'left': 'лево',
#         'down': 'право',
#         'right': 'низ'
#     }
# print(dictionary)
# print(dictionary['left'])
# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)
# for v in dictionary:
#     print(v)
# for v in dictionary:
#     print(dictionary[v])

# dictionary = {}
# dictionary = \
#     {
#         'up': 'верх',
#         'left': 'лево',
#         'down': 'право',
#         'right': 'низ'
#     }
# print(dictionary['up'])
# dictionary['left'] = 'ЛЕВО'  #меняет значения у кейсов
# print(dictionary['left'])
# del dictionary['down']       #удаляет элемент из словаря
# print(dictionary)
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# print(dictionary['up'])
# dictionary['up'] = 'UP'        #может изменять значения кейсов
# print(dictionary['up'])

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
# colors.add('gray')               #мы можем добавляет элементы в множество
# colors.add('red')                #если добавлять в множество элемент, который уже был, то ничего не изменится
# print(colors)
# colors.remove('red')             #мы можем удалять элемент из множества
# print(colors)
# colors.discard('blue')           #мы можем удалять значения из множества (это не вызовет ошибку, если нет такого, элемента, в отличии от оператора .remove())
# print(colors)
# colors.clear()                   #с помощью оператора .clear(), мы можем отчистить множество, и продолжить работать с пустым множеством)
# print(colors)

# a = {1, 2, 3, 5, 8}            #создаём первое множество
# b = {2, 5, 8, 13, 21}          #создаём второе множество
# c = a.copy()                   #копируем множество
# u = a.union(b)                 #объединяем два множества
# i = a.intersection(b)          #делаем пересечение множеств
# dl = a.difference(b)           #показывает разницу в двух множествах
# dr = b.difference(a)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# s = frozenset(a)               #создаёт из изменняемого множество, неизменяеммое, заморозка
# print(a)
# print(b)
# print(c)
# print(u)
# print(i)
# print(dl)
# print(dr)
# print(q)
# print(s)

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

list1 = [1, 2, 3, 4, 5]
print(len(list1))           #оператор len() показывает длину списка
print(list1.pop())          #оператор .pop() удаляет последний элемент из списка
print(list1.pop(2))         #оператор .pop(значение индекса) удаляет конкретный элемент из списка
print(list1.insert(2, 11))  #оператор .insert(значение индекса, значение аргумента) добавляет новый элемент, на выбранную позицию в списке
print(list1.append(12))     #оператор .append(значение аргумента) добавляет новый элемент в конец списка
print(list1)

