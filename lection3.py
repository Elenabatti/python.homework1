# def f(x):
#     return x**2

# g = f    
# print(f(4))
# print(g(4))    
# def calc(x):
#     return x * 10
# # print(calc(10))

# def calc2(x):
#     return x + 10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc, 10)
#  ------------------------------------------------ 
# LAMBDA


# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y +1
# def mult(x, y):
#     return x * y
# sum = lambda x, y: x * y
# def calc(op, a, b):
#     print(op(a,b))
#     return op(a,b)
# # calc(mult, 4, 5)
# calc(lambda x, y: x * y, 4, 5)


# LIST COMPREHENTION

# list = []

# for i in range(1,101):
#     # if i % 2 == 0:
#         list.append(i)
# print(list)        

# list = [(i, i) for i in range(1,21) if i % 2 == 0]
# print(list)


# def f (x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i % 2 ==0]
# print(list)
# path =input.txt
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)  

# def select(f,col):

#     return [f(x)for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x **2 ), res)
# print(res)


# li = [x for x in range(1,20)]
# li =list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# # print(data)
# for e in data:
#     print(e)


# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)        


# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#         list.append(i)
# print(list) 
#     return x**3



# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# def f(x):
#     return x**2
# list = [(i, f(i)) for i in range(1, 38) if i % 2 == 0]
# print(list)



# 35. В файле находится N н  атуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# with open('newfile.txt', 'r', encoding= 'utf - 8') as file:
#     some_list = file.read(). split()
#     print(some_list)
# some_list = list(map(int, some_list))
# new_list = [some_list[i]+1 for i in range(len(some_list)-1)if some_list[i]+1 !=some_list[i+1]]
# print(new_list)



# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:* [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3]
# from time import perf_counter
# start = perf_counter()
# import random
# some_list = [random.randint(1, 10) for i in range(10)]
# print (some_list)
# some_list.append(0)
# ind = 0
# res_list =[]
# temp_list =[]
# while ind < len(some_list) - 1:
#     if some_list[ind] < some_list[ind + 1]:
#         temp_list.append(some_list[ind])
        
#     else:
#         if len (temp_list) != 0:
#             temp_list.append(some_list[ind])
#             res_list.append(temp_list)
#             temp_list =[]
#     ind += 1
# print(res_list)
# end = perf_counter()
# print(end-start)             


# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# from time import perf_counter
# start = perf_counter()
# a = list(map(int, input().split()))
# for el in a:
#     if a.count(el) == 1:
#         print(el, end=' ')
# end = perf_counter()
# print(end-start)
# f = input().split()
# f1 =list(filter(lambda text:'а' not in text and 'б' not in text and 'с' not in text, f))
# print(f1)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

string = input()
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            count = 1
print(count, string[i])