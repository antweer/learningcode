#!/usr/bin/env Python3

from matplotlib import pyplot

def f(x):
	return x*x

xs = list(range(-100,101))
ys = []
for x in xs:
	ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.show()
