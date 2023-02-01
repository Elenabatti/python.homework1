# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# with open('input.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().split()
#     print(line)
#     maxx = int(line[0])
#     minn = int(line[0])
#     for el in line:
#         if int(el) > maxx:
#             maxx = int(el)
#         elif int(el) < minn:
#             minn = int(el)
#     print(minn, maxx)        


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

# with open('input.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().split()
#     a, b, c = int(line[0]), int(line[1]), int(line[2])
#     d = b ** 2 - 4 * a *c
#     if d < 0:
#         print('корней нет')
#     elif d == 0:
#         print(-b / 2 * a)
#         print((- b - d ** 0/5) / 2 *a)    


# 2) с помощью дополнительных библиотек Python
# a = 1
# b = 2
# c = 1
# import SymPy
# x = sympy.Symbol('x')
# print(sympy.solve(f'{a} * x ** 2 +{b} * x + {c}))