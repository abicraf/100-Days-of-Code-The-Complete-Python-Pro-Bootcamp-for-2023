############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = 'y'
first_round_flag = True
black_jack = False

def calculate_score(user_computer_score):
    sum = 0
    for card in user_computer_score:
        sum += card
    return sum

def check_result(user_score, computer_score):
    print(f"Your final hand: {user_card}, final score:  {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}\n")
    if user_score == 21:
        print(f"You win 😃. It's Black Jack!!!")
    elif user_score > 21:
        print(f"You lose 😭")
    elif computer_score > 21:
        print(f"You win 😃")
    elif user_score < computer_score:
        print(f"You lose 😭")
    elif user_score > computer_score:
        print(f"You win 😃")
    elif user_score == computer_score:
        print(f"Draw. 🙃")


def one_round(user_card, computer_card):
    user_score_went_over = False
    # computer_score_went_over = False
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    user_score, user_score_went_over = check_score_went_over(user_score, user_card)
    #computer_score, computer_score_went_over= check_score_went_over(computer_score, computer_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")
    return user_score, computer_score, user_score_went_over
    #return user_score, computer_score, user_score_went_over, computer_score_went_over

def check_score_went_over(sum, card_list):
    went_over = False
    if sum > 21:
        for score in card_list:
            if score == 11:
                sum = sum - 10
                went_over = False
                print(f"sum: {sum}, {card_list}")
            else:
                went_over = True
    return sum, went_over

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
while play == 'y':
    if first_round_flag:
        clear()
        print(logo)
        user_card = []
        computer_card = []
        user_score = 0
        computer_score = 0
        black_jack = False
        # if this is first round, user and computer get 2 cards
        for first_round in range(0, 2):
            user_card.append(random.choice(cards))
            computer_card.append(random.choice(cards))
        user_score, computer_score, user_score_went_over = one_round(user_card, computer_card)
        first_round_flag = False
        # check if user got blackjack
        if user_score == 21:
            black_jack = True
            check_result(user_score, computer_score)
            play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            first_round_flag = True
    # if this is not the first round, user and computer get 1 card
    while (black_jack == False) and (play =='y') and (first_round_flag == False):
        play = input("Type 'y' to get another card, type 'n' to pass:")
        if play == 'y':
                user_card.append(random.choice(cards))

                user_score, computer_score, user_score_went_over = one_round(user_card, computer_card)

                print(f"\nUser score went over? {user_score_went_over}\nUser_score: {user_score}\nComputer_score: {computer_score}\n")
        # check if user got blackjack
        if user_score == 21:
            black_jack = True
            check_result(user_score, computer_score)
            play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            first_round_flag = True
        elif (play == 'n') or (user_score > 21):
            while computer_score < 17:
                computer_card.append(random.choice(cards))
                computer_score = calculate_score(computer_card)
            check_result(user_score, computer_score)
            play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            if play == 'y':
                first_round_flag = True


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
