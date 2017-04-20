#!/usr/bin/env python3

from matplotlib import pyplot
from numpy import arange
import math

def f(x):
	return math.sin(x)

xs=arange(-5,6,0.1)
ys=[]

for x in xs:
	ys.append(f(x))

if __name__ == "__main__":
	pyplot.plot(xs,ys)
	pyplot.show()


