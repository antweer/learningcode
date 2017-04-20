#!/usr/bin/env python3

def playagain():
	answer = input("Do you want to play again(Y or N)?").lower()
	if answer == "y":
		return True
	else:
		return False

if __name__ == "__main__":
	print(playagain())


