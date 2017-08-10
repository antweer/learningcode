text = input("Text? ")
width = len(text) + 4

for num in range(0,3):
	if num == 0 or num == 2:
		print(width*"*")
	else:
		print("* " + text + " *")

	
