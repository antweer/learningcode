while True:
	import random
	secret_number = random.randint(1,10)
	tries = 5

	print("I am thinking of a number between 1 and 10.")
	while tries > 0:
		guess = int(input("What's the number? "))
		if guess == secret_number:
			print("Yes! You win!")
			break
		elif guess < secret_number:
			print("{} is too low.".format(guess))
			tries -= 1
			print("You have {} guesses left.".format(tries))
		elif guess > secret_number:
			print("{} is too high.".format(guess))
			tries -= 1
			print("You have {} guesses left.".format(tries))
		else: 
			print("You've managed to fuck up. Restart the program.")
	restart = input("Do you want to play again (Y or N)? ").lower()
	if restart == "n":
		print("Bye!")
		break
	elif restart != "y":
		print("Invalid input. Bye!")
		break



