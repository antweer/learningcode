height = int(input("Height: "))

for num in range(1,height+1):
	print(int(height-num)*" " + int(int(height*2-1)-2*int(height-num))*"*" + int(height-num)*" ")

