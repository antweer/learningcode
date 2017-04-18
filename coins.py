coins = 0

while True:
	print("You have {} coins.".format(coins))
	more = input("Do you want more coins? ").lower()
	if more == "yes":
		coins += 1
	elif more == "no":
		print("Bye.")
		break
	else:
		print("Invalid input. Please restart the program. Bye.")
		break



