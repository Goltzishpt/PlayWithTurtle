from turtle import *
from random import randint

# settings view and colors --------------------------------------------------------- #
hideturtle()                                                                         #
shape('classic')                                                                     #
speed(10)                                                                             #
Screen().colormode(255)                                                              #
Screen().bgcolor('skyblue')                                                          #
                                                           #
tracer(6, 0)                                                                         #
# ---------------------------------------------------------------------------------- #

# Decart --------------------------------------------------------------------------- #
goto(0, 300)                                                                       #
stamp()                                                                            #
write('y', font=('Arial', 20, 'bold'))                                             #
goto(0, 0)                                                                         #
goto(0, -300)                                                                      #
goto(0, 0)                                                                         #
goto(-300, 0)                                                                      #
goto(0, 0)                                                                         #
goto(300, 0)                                                                       #
stamp()                                                                            #
write('x', font=('Arial', 20, 'bold'))                                             #
goto(0, 0)                                                                         #
# ---------------------------------------------------------------------------------- #


def square(n, color):  # функция, которая рисует квадрат, задаем размер и цвет заранее
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(n)
        left(90)
    end_fill()


def check(size, color):  # функция, которая рисует первые 4 ряда
    for x in range(-size, size, int(size/2)): # вот такой вот шаг задает нам положение от первой точки Х до последней
        for y in range(-size, size, int(size/2)): # вот такой вот шаг задает нам положение от первой точки У до последней
            penup()
            goto(x, y)
            pendown()
            square(int(size/4), color)

def mate(size, color): # функция, которая рисует вторые 4 ряда
    for x in range(-size+int(size/4), size+int(size/4), int(size/2)): # а вот такой шаг задает нам положение Х в шахматном порядке
        for y in range(-size+int(size/4), size+int(size/4), int(size/2)): # а вот такой шаг задает нам положение У в шахматном порядке
            penup()
            goto(x, y)
            pendown()
            square(int(size/4), color)
    penup()  # это просто квадратик чтобы обвести
    goto(-size, -size)
    pendown()
    for _ in range(4):
        forward(size*2)
        left(90)


# цикл ащиты от дурака. можно и меньше 200, но будет такое себе, а больше 400
# не влазит в экран. если есть остаток от деления на 2, то выходит абракадабра
a = 0
while a == 0:
    row = int(input('Введите четное число от 200 до 400: '))
    if 199 < row and row < 401 and row % 2 == 0:
        color = [randint(0, 255) for _ in range(3)]
        check(row, tuple(color))
        mate(row, tuple(color))
        Screen().setup(row*2+40, row*2+40) # размер экрана с хвостиком
        a = 1
    else:
        continue


done()
