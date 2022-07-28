print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

people = int(input("How many people to split the bill? "))

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = total_bill * percentage/100

total = tip + total_bill

split = total/people

print("Each person should pay: $%.1f"%split)

