#!/usr/bin/env python3

from turtle import *
import shapes2

up()
goto(-225,180)
down()
shapes2.triangle(50,True,"red")
up()
forward(150)
down()
shapes2.square(75,False,"red")
up()
forward(150)
down()
shapes2.pentagon(80, True, "violet")
up()
goto(-225,30)
down()
shapes2.hexagon(75, False, "black")
up()
forward(150)
down()
shapes2.octagon(50, True, "green")
up()
forward(150)
down()
shapes2.star(75, True, "yellow")
up()
right(90)
forward(200)
down()
shapes2.circle2(25, False, "red")

mainloop()

