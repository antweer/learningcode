#!/usr/bin/env python3

from turtle import *

def dt(size, fill, c):
	color(c)
	if fill == True:
		begin_fill()
	down()
	for i in range(3):
		forward(size)
		right(120)
	end_fill()
	up()
	right(60)
	forward(size)
	left(60)
	
def ut(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	down()
	for i in range(3):
		forward(s)
		left(120)
	end_fill()
	up()
	left(60)
	forward(s)
	right(60)

def square(s, f, c):
	color(c)
	if f == True:
		begin_fill()
	for i in range(4):
		forward(s)
		right(90)
	end_fill()

def pentagon(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	for i in range(5):
		forward(s)
		right(72)
	end_fill()

def hexagon(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	for i in range(6):
		forward(s)
		right(60)
	end_fill()

def octagon(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	for i in range(8):
		forward(s)
		right(45)
	end_fill()

def star(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	for i in range(5):
		forward(s)
		right(144)
	forward(0.375*s)
	for i in range(5):
		forward(.25*s)
		right(72)
	end_fill()

def circle2(s,f,c):
	color(c)
	if f == True:
		begin_fill()
	circle(s)
	end_fill()


