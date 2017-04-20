#!/usr/bin/env python3

from matplotlib import pyplot

def f(x):
	if x%2 == 0:
		return -1
	elif x%2 == 1:
		return 1

xs = list(range(-5,6))
ys = []

for x in xs:
	ys.append(f(x))

if __name__ == "__main__":
	pyplot.bar(xs,ys)
	pyplot.show()


