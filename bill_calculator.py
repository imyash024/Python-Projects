# Prints the Welcome Statement
print("Welcome to the tip calculator!")
# take input from the user bill amount then convert it into the floating point number as in python every input is treated as string. similarly tip and no of people is taken as input
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# calculation of the bill 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# rounding off the bill to nearest 2 point decimal number using round function.
final_amount = round(bill_per_person, 2)
# Output : Each Person's bill
print(f"Each person should pay: ${final_amount}")