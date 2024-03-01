
import random

def roll():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value, max_value)

    return roll

# value = roll()
# print(value) no

while True:
    players = input("Enter the number of the players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players .")
    else:
        print("Invalid. try again.")

# print(players)

max_score = 50
# list compreshension
# which puts a zero inside of the list for every single player that we have.
# i lekhna mi milyo but here is underscore _ j lekhe ni hunchha
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number ",player_idx + 1, "turn has just started !\n")
        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y) ??")
            if should_roll.lower()=="y":
                break

            value = roll()
            if value == 1:
                print("YO rolled a 1 ! Tero palo sakkiyo")
                current_score = 0
                break
            else:
                current_score += value
                print("Yo rolled a:", value)

            print("Your score is:", current_score)
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

        
