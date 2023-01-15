#  Задача 22
#  Задайте список из нескольких чисел. Напишите программу, которая найдёт
#  сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# a = input().split()
# sum = 0
# for i in range(len(a)):
#     if i % 2 != 0:
#         sum += int(a[i])
#     print(sum)

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")
# summa = 0
# some_list = input().split()
# for ind in range(1, len(some_list), 2):
#     summa += int(some_list[ind])
# print(summa)    

# Задание 23
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# some_list = input().split()
# new_list = []
# for start in range(0, (len(some_list) -1) // 2 +1):
#     new_list.append(int(some_list[start]) * int(some_list[len(some_list) - start -1]))
# print(new_list)    

# Задача 24
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# some_list = input().split()
# maxx = 0
# minn = 1
# for el in some_list:
#     if'.' in el:
#         number = el.split('.')[1]
#         if int(number) !=0:
#             if float('0.' + number) < minn:
#                 minn = float('0.'+ number)
#             elif float('0.' + number) > maxx:
#                     maxx = float('0.' + number)
# print(maxx - minn)       

# some_list = input().split()
# maxx = 0
# minn = 1
# for el in some_list:
#     if float(el) % 1 != 0:
#         if float(el) % 1 < minn:
#             minn = float(el) %1
#         if float(el) % 1 > maxx:
#             maxx = float(el) % 1
# print(round(maxx - minn, 2))                             

# Задача 25
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = int(input())
# out_str = ''
# while n > 0:
#     out_str = str(n % 2) + out_str
#     n //= 2
# print(out_str)


# решение со списком
# n = int(input())
# out_list = []
# while n > 0:
#     out_list.append(str(n % 2))
#     n //= 2
# out_list.reverse()
# print(*out_list, sep='')
# 

# Задача 26.
# Задайе число. Составьте список фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для к = 8

# k = int(input())
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# some_list[k - 1] = 1
# for ind in range(k + 2, k * 2 + 1):
#     some_list[ind] = some_list[ind - 1] + some_list[ind -2]
# for ind in range(k - 2, k - 1 - 1):
#     some_list[ind] = some_list[ind + 2] - some_list[ind + 1]   
# print(some_list)  



