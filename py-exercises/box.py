width = int(input("Width? "))
height = int(input("Height? "))

for num in range(0,height):
	if num == 0 or num == height-1:
		print(width*"*")
	else:
		print("*" + int(width-2)*" " + "*")

