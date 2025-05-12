print("Welcome to Python Pizza Deliveries!")

# takes size, pepperoni and extra cheese choices as an input.
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# based on choice of user, bill is calculated using if else conditional statements.
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

# bill is displayed to the user.
print(f"Your final bill is: ${bill}.")


