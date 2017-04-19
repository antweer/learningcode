#1 Uppercase a String
a="Tanweer"
print(a)
print(a.upper())

#2 Capitalize a String
b="rajwani"
print(b)
print(b.capitalize())

#3 Reversing a String

print(b)
print(b[::-1])

#4 Leetspeak

c="Hello, how are you? I'm good, how about yourself? Cool, have a nice day!"
d=""

for num1 in range(0,len(c)):
	if c[num1].upper()  == "A":
		d = d + "4"
	elif c[num1].upper() == "E":
		d = d + "3"
	elif c[num1].upper() == "G":
		d = d + "6"
	elif c[num1].upper() == "I":
		d = d + "1"
	elif c[num1].upper() == "O":
		d = d + "0"
	elif c[num1].upper() == "S":
		d = d + "5"
	elif c[num1].upper() == "T":
		d = d + "7"
	else:
		d = d +  c[num1]

print(c)
print(d)

#5 Long-long Vowels
"""
e="Good"
f=""

for num2 in range(0,len(e)):
	if e[num2].lower() == "a" and e[num2+1] == e[num2]:
		f = f + 4*e[num2]
	elif e[num2].lower() == "e" and e[num2+1] == e[num2]:
                f = f + 4*e[num2]
        elif e[num2].lower() == "i" and e[num2+1] == e[num2]:
                f = f + 4*e[num2]
        elif e[num2].lower() == "o" and e[num2+1] == e[num2]:
                f = f + 4*e[num2]
        elif e[num2].lower() == "u" and e[num2+1] == e[num2]:
                f = f + 4*e[num2]
	else:
		f = f + e[num2]

print(e)
print(f) 
""" 
#Simpler solution

word = "cheese"
word = word.replace("aa", "aaaaa")
word = word.replace("ee", "eeeee")
word = word.replace("ii", "iiiii")
word = word.replace("oo", "ooooo")
word = word.replace("uu", "uuuuu")

print(word)

#6 Caesar Cipher

g="lbh zhfg hayrnea jung lbh unir yrnearq"
h=""
j=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for num3 in range(0,len(g)):
	if j.count(g[num3]) == 1:
		h= h + j[j.index(g[num3])-13]
	else:
		h = h + g[num3]
print(g)
print(h)

