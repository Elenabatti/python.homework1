# def f(x):
#     if x == 1:
#         return 'целое'
#     elif x ==2.3:
#         return 23
#     else:
#         return


#Recursion. Последовательность фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) +fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

#кортежи
# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])
# a[0] = 12

# a = (3, 4, 5)
# for item in a:
#     print(item)

#Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': '1'
#         'down': '3'
#         'right': '4'
#     }

# for k in dictionary.values():
#     print(k)

some_dict = {1: 25}


# Множeства
#  По множесту нельзя пройти циклом и нет индексов
# b = {1, 2, 3, 4, 5}
# a = set()
# a.add(10)
# print(a)
# print(b)


# import random
# import time
# a = [random.randint(0, 10 * 6) for _ in range(10**6)]
# b = set(a)

# start = time.perf_counter()
# print(110 in a)
# end = time.perf_counter()
# start1 = time.perf_counter()
# print (110 in b)
# end1 = time.perf_counter()
# print((end - start) / (end1 - start1))

# Списки
# list1 = [1,2,3,4,5]
# list1[0] = 123

# list2 = list1
# list2[1] = 222
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)    
# list1[0] = 123

# как можно удалить последний элемент из списка
# list1 = [1,2,3,4,5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)


#  Как удалить необходимый элемент из списка, путем указывания конкретного индекса
# list1 = [1,2,3,4,5]

# print(list1.pop(2))
# print(list1)

#Как добавить элементв список
# list1 = [1,2,3,4,5]

# print(list1.insert(2, 11))
# print(list1)


# Просто добарвление в конец делается через  append
# list1 = [1,2,3,4,5]

# print(list1.append(11))
# print(list1)