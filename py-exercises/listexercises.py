#1 Sum the Numbers
a=[3,5,6,2,5,7,8,2,12,45]
print(a)

asum = sum(a)
print(asum)

#2 Largest Number

a.sort(reverse = True)
alargest = a[0]
print(alargest)

#3 Smallest Number

a.sort()
asmallest = a[0]
print(asmallest)

#4 Even Numbers
b=[-36,-23,-20,-15,-10,-6,-3,0,2,3,4,5,7,8,10,11,14,15,18,19,22,29,32,35]
print(b)

for num1 in range(0,len(b)):
	if b[num1]%2 == 0:
		print(b[num1])
	else:
		continue

#5 Positive Numbers

for num2 in range(0, len(b)):
	if b[num2]>0:
		print(b[num2])
	else:
		continue

#6 Positive Numbers II

c=[]

for num3 in range(0, len(b)):
	if b[num3]>0:
		c.append(b[num3])
	else:
		continue
print(c)

#7 Multiply a list

f=2
d=[]

for num4 in c:
	d.append(num4*f)
print(d)

#8 Multiply Vectors


e=[2,3,4]
f=[6,7,8]
g=[]
print(e)
print(f)

if len(e) == len(f):
	for num5 in e:
		g.append(num5*f[e.index(num5)])
print(g)


#9 Matrix Addition

h=[[3,4],[6,7]]
i=[[4,6],[8,9]]
j=[[0,0],[0,0]]

for num6 in range(0,len(h)):
        for num7 in range(0,len(h[num6])):
                j[num6][num7]=h[num6][num7]+i[num6][num7]

print(h)
print(i)
print(j)

#10 Matrix Addition II - See #9

#11 De-dup

k=[2,2,2,3,4,1,5,6,7,7,5,6,8,9]

l=[]
for num8 in range(0,len(k)):
	if l.count(k[num8]) == False:
		l.append(k[num8]) 
	else:
		continue
print(k)
print(l)

#12 Matrix Multiplication

#[[0][0]*[0][0]+[0][1]*[1][0],[0][0]*[0][1]+[0][1]*[1][1]],...

m=[[2,3],[5,6]]
n=[[3,4],[4,3]]
o=[[0,0],[0,0]]

o[0][0] = m[0][0]*n[0][0] + m[0][1]*n[1][0]
o[0][1] = m[0][0]*n[0][1] + m[0][1]*n[1][1]
o[1][0] = m[1][0]*n[0][0] + m[1][1]*n[1][0]
o[1][1] = m[1][0]*n[0][1] + m[1][1]*n[1][1]

print("{} * {} ={}".format(m,n,o))


