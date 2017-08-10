day = int(input("Day (0-6)? "))

if day <= 5 and day >= 1:
	print("Go to work")
elif day == 0 or day == 6:
	print("Sleep in")
else:
	print("Please enter a number between 0-6")

