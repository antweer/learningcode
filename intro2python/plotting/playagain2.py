#!/usr/bin/env python3

def playagain():
	while True:
		answer = input("Do you want to play again(Y or N)?").lower()
		if answer == "y":
			return True
			break
		elif answer == "n":
			return False
			break
		else:
			print("Invalid input.")
			continue

if __name__ == "__main__":
	print(playagain())


