#!/usr/bin/env python3

from matplotlib import pyplot
import math

def f(x):
	return math.sin(x)

xs=list(range(-5,6))
ys=[]

for x in xs:
	ys.append(f(x))

if __name__ == "__main__":
	pyplot.plot(xs,ys)
	pyplot.show()


