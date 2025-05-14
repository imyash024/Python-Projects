# Understanding if else and elif conditionals 

# ascii arts using ascii arts website

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# prints welcome statement 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
# asks the user for the direction
direction = input("     Type \"left\" or \"right\"")

# if user types left then game continues else prints wrong direction and Game over. There is lower function in python which converts every character of string into lower case. It is good to convert the input into lower case so that in case user inputs into uppercase or title case then too then game continues rather then showing game over to the user

if direction.lower() == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    # After opting for left user to asked to wait or swim
    action_choice = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    # if user opts for wait then he arrives at the island else he is eaten by crocodiles and game ends.
    if action_choice.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        # After reaching island user is prompted to choose one of three doors encountered red, yellow and blue
        color_choice = input("    One red, one yellow and one blue. Which colour do you choose?")
        # if user opts for yellow he gets the treasure and wins the game else game over
        if color_choice.lower() == "yellow":
            print("YOU WON!!!")
        else:

            print("Game Over.")

    else:
        print("Crocodiles have attacked you.")
        print("Game Over.")
else:
    print("Wrong direction.\nGame Over.")
