print("Welcome to the tip calculator\n")
bill = float(input("What is the total bill in Euro?\n"))
tip = int(input("What percentage would you like to tip? 10, 12 or 15?\n"))
split = int(input("How many people to split the bill?\n"))

tip_percentage =  tip / 100
tip_total = bill * tip_percentage
bill_total = bill + tip_total
payment = bill_total / split
payment_final = round(payment, 2)

print(f"Each person has to pay {payment_final}€")