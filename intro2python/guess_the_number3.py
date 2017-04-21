attempt = 1
low = 0
high = 100
guess = 50

while True:
	print("I'm guessing that your number is {}".format(guess))
	feedback = input("How was my guess? (high, low, or correct) ").lower()
	if feedback == "correct":
		print("Wow! I guessed your number in {} attempt(s).".format(attempt))
		break
	elif feedback == "high":
		high = guess
		guess = int(int(high+low)/2)
		attempt += 1
	elif feedback == "low":
		low = guess
		guess = int(int(high+low)/2)
		attempt +=1
	else:
		print("Invalid input. Game will end, please restart. Bye!")
		break




