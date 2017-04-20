#!/usr/bin/env python3

from turtle import *
import shapes2
import random

numstars = int(input("How many stars do you wish to see in the sky tonight? "))

bgcolor("black")
speed(0)

for x in range(0,numstars):
	up()
	goto(random.randint(-275,275),random.randint(-250,250))
	down()
	shapes2.star(random.randint(10,40),True,"yellow")

mainloop()


