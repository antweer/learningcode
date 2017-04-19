x = int(input("What do you want to factorize? "))

for num in range(1,x+1):
	if x%num == 0:
		print(num)
	else:
		continue

