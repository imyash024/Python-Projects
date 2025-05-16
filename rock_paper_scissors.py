# importing random module as the name suggest it pick out random number or item from the list or dictionary.
import random

# ascii art from ascii art website
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# prompt the user to input his choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# computer uses random module to choose randomly.
computer_choice= random.randint(0,2)

# using elif ladder, the logic of the game is coded.
if user_choice == 0:
    print(rock)
    if computer_choice == 0:
        print("Computer Choose:\n")
        print(rock)
        print("Draw")
    elif computer_choice == 1:
        print("Computer Choose:\n")
        print(paper)
        print("You lose")
    elif computer_choice == 2:
        print("Computer Choose:\n")
        print(scissors)
        print("You Won")
if user_choice == 1:
    print(paper)
    if computer_choice == 0:
        print("Computer Choose:\n")
        print(rock)
        print("You Won")
    elif computer_choice == 1:
        print("Computer Choose:\n")
        print(paper)
        print("Draw")
    elif computer_choice == 2:
        print("Computer Choose:\n")
        print(scissors)
        print("You lose")
if user_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print("Computer Choose:\n")
        print(rock)
        print("You lose")
    elif computer_choice == 1:
        print("Computer Choose:\n")
        print(paper)
        print("You Won")
    elif computer_choice == 2:
        print("Computer Choose:\n")
        print(scissors)
        print("Draw")