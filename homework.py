# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
#  пример: 6 - да. 1 - нет

# number1 = int(input('введите цифру, обозначающую день недели:'))
# if number1 == 6 or number1 == 7:
#     print('да')
# else:
#     print('нет')



# 8. Напишите программу, которая принимает на вход координаты точки(X и Y) причем X не = 0 и Y не равно 0 
# и выдаёт номеи четверти плоскости, в которой находится эта точка(или на какой оси она находится)

# x = int(input())
# y = int(input())
# if x == 0 and y == 0:
#     print('x и y не должны быть ровны 0')
# elif x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# else:
#     print('4')


# 9. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти(x и y)

# z = int(input())
# if z == 1:
#     print('x > 0 and y > 0')
# elif z == 2:
#     print('x < 0 and y > 0')
# elif z == 3:
#     print('x < 0 and y < 0')
# elif z == 4:
#     print('x > 0 and y < 0')
# else:
#     print('введите корректные данные')

# 10. Напишите программу, которая принимает на вход координаты 2х точек и находит расстояние между ними в 2D пространстве

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ac = y1 - y2
bc = x2 - x1
print((ac ** 2 + bc ** 2) ** 0.5)
