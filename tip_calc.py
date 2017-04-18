bill = float(input("Total bill amount? "))
service = input("Level of service? (good, fair, bad) ").lower() 

if service == "good":
	tip = bill*.20
	total = bill + tip
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
elif service == "fair":
	tip = bill*.15
	total = bill + tip
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
elif service == "bad":
	tip = bill*.10
	total = bill + tip
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
else:
	print("I'm sorry. Please restart the program.")
