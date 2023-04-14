from art import logo, vs
from game_data import data
import replit
import random

# define variable
compare_name_a = ''
compare_name_b = ''
compare_description_a = ''
compare_description_b = ''
compare_follower_a = ''
compare_follower_b = ''
compare_country_a = ''
compare_country_b = ''
score = 0
continue_game = True
first_comparison = True

# define a function to get data Compare_A and Compare_B from game_data.data{}
# check the result and if this is the right guess
# calculate score. if correct then "score += 1"
def compare(user_guess, user_score, follower_a, follower_b, continue_game):
    # compare the follower count
    if follower_a > follower_b:
        answer = 'a'
    elif follower_b > follower_a:
        answer = 'b'

    # clear screen
    # print the logo and the score
    replit.clear()
    print(logo)
    # compare the answer and the guess
    if answer == user_guess:
        user_score += 1
        print(f"You're right! Current score: {user_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        continue_game = False

    return user_score, continue_game




# define a function to randomly choose A and B from data
def random_choose():
    name = ''
    description = ''
    country = ''
    followers = ''
    data_set = random.choice(
        data)  #return a randomly picked dictionary from data[]
    # print (data_set) # data_set{} is a dictionary type
    # print(data_set.values())
    # print(data_set.keys())
    for index in data_set:
        #*******  "i" is the key, print key and value out from the dictionary *******
        # for i in d:
        #     print i, d[i]
        if index == 'name':
            name = data_set[index]
        if index == 'description':
            description = data_set[index]
        if index == 'country':
            country = data_set[index]
        if index == 'follower_count':
            followers = data_set[index]
    return name, description, country, followers



# program start:

print(logo)
while continue_game == True:
    # if this is the first comparision, then randomly choose Compare_A
    # if not, then replace Compare_A with Compare_B
    # print the name and info. e.g.: Compare A: Shakira, a Musician, from Colombia.
    if first_comparison == True:
        compare_name_a, compare_description_a, compare_country_a, compare_follower_a = random_choose(
        )
        first_comparison = False
    else:
        compare_name_a, compare_description_a, compare_country_a, compare_follower_a = compare_name_b, compare_description_b, compare_country_b, compare_follower_b
    print(
        f"Compare A: {compare_name_a}, a {compare_description_a}, from {compare_country_a}. {compare_follower_a}"
    )

    print(vs)
    # print the name and info. e.g.: Against B: UEFA Champions League, a Club football competition, from Europe
    # check if the compare_name_a is the same as compare_name_b, if yes, then random_choose again.
    compare_name_b = compare_name_a
    while compare_name_b == compare_name_a:
        compare_name_b, compare_description_b, compare_country_b, compare_follower_b = random_choose(
        )
    print(
        f"Against B: {compare_name_b}, {compare_description_b}, from {compare_country_b}.  {compare_follower_b}"
    )

    # ask user to guess who has more followers
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # compare Compare_A and Compare_B
    # if wrong, then end the game, print out the final score.
    # if right, print the current score.
    # use a loop to start over the game.(no need to clear the screen)
    # Continue the game from "Compare A: Neymar, a Footballer, from Brasil." and print vs string

    score, continue_game = compare(user_guess = guess, user_score = score, follower_a = compare_follower_a, follower_b = compare_follower_b, continue_game = continue_game)
