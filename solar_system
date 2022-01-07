from turtle import *
from math import tan, radians, sqrt, sin, cos
from random import randint

# settings view and colors --------------------------------------------------------- #
hideturtle()                                                                         #
shape('classic')                                                                     #
speed(10)                                                                             #
Screen().colormode(255)                                                              #
Screen().bgcolor('skyblue')                                                          #
Screen().setup(1500, 500)                                                            #
tracer(6, 0)                                                                         #
# ---------------------------------------------------------------------------------- #
'''
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
'''
planet = {'Sun': ['yellow', 100, -500, -100], 'Mercury': ['burlywood', 10, -250, -10],
          'Venus': ['burlywood', 20, -200, -20], 'Earth': ['darkolivegreen', 10, -130, -10],
          'Mars': ['brown1', 30, -60, -30], 'Jupiter': ['burlywood', 60, 120, -60],
          'Saturn': ['burlywood', 55, 280, -55], 'Uran': ['cadetblue', 40, 420, -40],
          'Neptun': ['cornflowerblue', 35, 530, -35], 'Pluto': ['burlywood', 10, 600, -10]}

penup()
goto(-500, -520)
pendown()
circle(520)
for i in planet:
    penup()
    goto(planet[i][2]-10, planet[i][3]-20)
    write(i)
    goto(planet[i][2], planet[i][3])
    pendown()
    fillcolor(planet[i][0])
    begin_fill()
    circle(planet[i][1])
    end_fill()
    if i == 'Saturn':
        a, b = 60, 28.5
        penup()
        goto(a * sin(radians(60)) + 280, b * cos(radians(60)))
        pendown()
        for deg in range(60, 300):
            rad = radians(deg)
            x = a * sin(rad) + 280
            y = b * cos(rad)
            goto(x, y)

done()
