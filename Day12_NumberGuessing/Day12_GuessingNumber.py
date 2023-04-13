#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

attempt_time = 0
guess = []
answer = random.randrange(1, 101)  # Random Integer from 1 to 100 inclusive
#another way is randint(1,100) from 1 to 100


def guess_number(attempt_time):
    '''guess number function'''
    # guess the number "attmpts_time" times
    Correct = False
    while (Correct == False) and (attempt_time != 0):
        #present the reminning guesses and then subtract one tme
        print(
            f"You have {attempt_time} remaining to guess the number in easy mode "
        )
        attempt_time -= 1

        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"Correct!! The answer is {answer}")
            Correct = True
        elif guess < answer:
            print(f"Too low. Guess again.\n")
        elif guess > answer:
            print(f"Too high. Guess again.\n")

    if attempt_time == 0:
        print("\nRun out of turns.")


print(logo)
print(
    "Welcome to the number guessing game!\n Submit a guess for a number between 1 and 100."
)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    guess_number(attempt_time=10)
elif level == 'hard':
    guess_number(attempt_time=5)
# print(f"{answer}")
