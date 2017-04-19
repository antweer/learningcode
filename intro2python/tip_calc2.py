bill = float(input("Total bill amount? "))
service = input("Level of service? (good, fair, bad) ").lower() 
split = float(input("Split how many ways? "))

if service == "good":
	tip = bill*.20
	total = bill + tip
	if split > 0: 
		perperson = total/split
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
	print("Amount per person: ${:.2f}".format(perperson))
elif service == "fair":
	tip = bill*.15
	total = bill + tip
	if split > 0: 
		perperson = total/split
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
	print("Amount per person: ${:.2f}".format(perperson))
elif service == "bad":
	tip = bill*.10
	total = bill + tip
	if split > 0: 
		perperson = total/split
	print("Tip amount: ${0:.2f}".format(tip))
	print("Total amount: ${0:.2f}".format(total))
	print("Amount per person: ${:.2f}".format(perperson))
else:
	print("I'm sorry. Please restart the program.")
