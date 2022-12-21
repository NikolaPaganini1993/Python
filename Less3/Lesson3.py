# # 1. Анонимные, lambda функции


# # Обычная функция (summa()) принимает только одну
# # переменную (x).
# def summa(x):
#     x = x + 10
#     return x
# print(summa(2))


# # Но иногда нам надо сделать много однотипных
# # функций, тогда мы можем создать
# # функцию(math()) с функциями (calc1(), calc2())
# # и переменной (x).
# def calc1(x):
#     return x+10
#
# def calc2(x):
#     return x*10
#
# def math(op, x):
#     print(op(x))
#
# math(calc1, 10)
# math(calc2, 5)


# # Бывают функции (summa()) с двумя переменными (x, y)
# def summa(x, y):
#     return x + y
#
# def mult(x, y):
#     return x * y


# # Мы также можем соединить эти две функции(summa(),
# # mult()), в одну calc()
# def calc(op, a, b):
#     return(op(a, b))


# # В качестве аргумента (op) может быть целая функция,
# # например: mult()
# print(calc(mult, 4, 5))

# # Чтобы упростить код можно не расписывать всю функцию,
# # а воспользоваться lambda. Например:
#  def summa(x, y):
#      return x + y


# # Всю эту функцию можно заменить на:
#
# summa = lambda x, y: x + y


# # С точки зрения Python, это абсолютно одиннаковые строки.
# def calc(op, a, b):
#     return(op(a, b))
# print(calc(summa, 4, 5))


# Чтобы еще сократить код, можем закинуть эту lambda функцию
# в вывод результата.
# def calc(op, a, b):
#     return(op(a, b))
# print(calc(lambda x, y: x + y, 4, 5))


# # 2. List Comprehension
# # [exp for item in iterable]
# # exp = выражение item = порядковый номер iterable = объект
# # [exp for item in iterable (if conditional)]
# # Если требуется какая - то выборка, то используем if conditional
# # [exp <if conditional> for item in iterable(if conditional)]


# # Чтобы создать список от 1 до 100 cо счетными числами.
# # Мы можем создать список (list = []), и пробежаться по каждому
# # его элементу (for i in range(1, 101)), затем добавить условие
# # (x % 2 == 0), и добавить подходящие числа в созданный список
# # (list.append(i)).
# list = []
# for i in range(1, 21):
#     if(i % 2 == 0):
#         list.append(i)
# print(list)


# # Но мы можем сделать этот код короче, благодаря List Comprehension.
# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)


# # Если мы хотим создать кортеж в списке, нужно вместо аргумента (i),
# # добавить кортеж (i, i)
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list)


# # Мы можем аргумент, заменить на функцию,
# # и у нас будут обрабатываться данные.
# def f(x):
#     return x**3
#
# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)


# # Мы можем вместо аргумента подставить кортеж, со вложенной
# # функцией.
# def f(x):
#     return x**3
#
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)


# # Задача.
# # В файле хранятся числа, нужно выбрать четные и составить
# # список пар (число, квадрат числа)
# path = 'C:/Python/Less1/Less3/file.txt'    #указываем путь к файлу
# f = open(path, 'r')                        #при помощи open(), открываем его, и добавляем 'r' указывая на то, что этот файл только для чтения
# data = f.read() + ' '                      #считываем всё что есть, и добавляем пробел
# f.close()                                  #закрываем файл
#
# numbers = []
#
# while data != '':                          #делаем проверку, пока наша строка не пустая ( != '')
#     space_pos = data.index(' ')            #находим первую позицию пробела
#     numbers.append(int(data[: space_pos])) #проверяем от позиции первого символа до позиции пробела (data[: space_pos)
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)


# # С помощью lambda и list comperension, мы можем сделать этот код проще.
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)


# # 3. Функция map.
# # Функция map() применяет указанную функцию к каждому элементу
# # итерируемого объекта и возвращает итератор с новыми объектами.
# # f(x) -> x + 10
# # map(f, [ 1,  2,  3,  4])
# #        [11, 12, 13, 14]
# my_list = [x for x in range(1, 20)]      #создаём список от 1 до 20
# print(my_list)                           #выводим список
# my_list = map(lambda x: x + 10, my_list) #с помощью функции map() применяем указанную функцию (x + 10) к каждому элементу списка (my_list)
# print(my_list)                           #выводим обновленный список
# my_list_2 = list(my_list)                #с помощью функции list() применяем к нашим данным тип списка
# print(my_list_2)                         #выводим окончательный список

# # С помощью функции map(), можно преобразовать каждый элемент
# # списка в натуральное число (int)
# data = list(map(int, input().split()))
# print(data)


# data = map(int, '1 2 3'.split())
# for i in data:
#     print(i)

# # С помощью map(), мы можем сделать этот код проще.
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# # 4. Filter()
# # Функция filter() применяет указанную функцию к каждому элементу
# # итерируемого объекта и возвращает итератор с теми объектами, для
# # которых функция вернула True.
# # f(x) -> x - чётное
# # filter(f, [1, 2, 3, 4])
# #           [   2,    4]


# data = [x for x in range(10)]                #создаём список
# result = filter(lambda x: x % 2 == 0, data)  #с помощью filter(), подвергаем каждый элемент списка (data) проверке (x % 2 == 0), если условие выполняется, оставляем проверяемый элемент в списке
# result2 = list(result)                       #фунция filter, преобразовывает тип нашего списка в filter объект, чтобы получить обратно список, воспользуемся оператором list()
# print(result2)


# # С помощью filter(), мы можем сделать наш код проще.
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# # 3. Функция zip.
# # Функция zip() применяется к набору итерируеммых объектов
# # и возвращает итератор с кортежами из элементов входных данных.
# # Количество элементов в результате равно минимальному количеству
# # элементов входного
# # zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
# #     ([1, 'о', 'f'], [2, 'д', 's'], [3, 's', 'т'])


# users = ['user1', 'user2', 'user3', 'user4', 'user5'] #создаём список1
# ids = [4, 5, 9, 14, 7]                                #создаём список2
# data = zip(users, ids)                                #с помощью zip(), соединияем два списка (users и ids), каждый элемент с каждым по порядку, в результате получим кортеж из двух элементов
# data = list(zip(users, ids))                          #фунция zip, преобразовывает тип наших данных в zip объект, чтобы получить обратно список, воспользуемся оператором list()
# print(data)


# # 4. Функция enumerate.
# # Функция enumerate() применяется к итерируемому объекту
# # и возвращает новый итератор с кортежами из индекса и
# # элментов входных данных.
# # enumerate (['Казань', 'Смоленск', 'Рыбки'], 'Чикаго'])
# #           [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = enumerate(users)
# data = list(data)
# print(data)