#!/usr/bin/env python3

from matplotlib import pyplot

def f(x):
	return x*1.8 + 32

cel=list(range(-5,6))
far=[]

for x in cel:
	far.append(f(x))

if __name__ == "__main__":
	pyplot.plot(cel,far)
	pyplot.show()


