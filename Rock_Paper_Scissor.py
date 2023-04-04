import random

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

#Write your code below this line
items = [rock, paper, scissors]
#print(type(items))
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
  print("Type the wrong number!")
else:
    print(items[user_choice])

    print("Computer Chose:\n")
    computer_choice = random.randint(0,2)
    print(items[computer_choice])
    #print(computer_choice)

    if user_choice == 1 and computer_choice == 0: # Paper vs Rock
      print("You Win!!!")
    elif user_choice == 2 and computer_choice == 1: # Scissors vs Paper
      print("You Win!!!")
    elif user_choice == 0 and computer_choice == 2: # Rock vs Scissors
      print("You Win!!!")
    elif user_choice == computer_choice:
      print("It's a draw. Once again?")
    else:
      print("You Lose...")
