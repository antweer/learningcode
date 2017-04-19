attempt = 1
guess = 50
guess1 = 50

while True:
	print("I'm guessing that your number is {}".format(guess))
	feedback = input("How was my guess? (too high, high, too low, low, or correct) ").lower()
	if feedback == "correct":
		print("Wow! I guessed your number in {} attempt(s).".format(attempt))
		break
	elif feedback == "too high":
		guess1 = int(guess1/2)
		guess = int(guess - guess1)
		attempt += 1
	elif feedback == "too low":
		guess1 = int(guess1/2)
		guess = int(guess + guess1)
		attempt +=1
	elif feedback == "high":
		guess = int(guess - 1)
		attempt +=1
	elif feedback == "low":
		guess = int(guess + 1)
		attempt +=1
	else:
		print("Invalid input. Game will end, please restart. Bye!")
		break




