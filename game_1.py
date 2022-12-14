# count upto 100

# A game where you and AI will take random numbers from 1-10.
# Your task is to make the sum go to 100.

# Libraries
import random
import time

# Variables
total_sum = 100
user_sum = 0
ai_sum = 0
total = 0
running = True
player_turn = True

while running:
    user = int(input("Take any number from 1 to 10: "))

    if user > 10 or user < 1:
        print("Please give the correct input")
        continue
    else:
        user_sum += user
        player_turn = not player_turn

    ai = random.randint(1, 10)
    ai_sum += ai

    total = user_sum + ai_sum

    print(f'"User" choose {user} and "AI" choose {ai}\n')
    print(f"Total sum is {total}")

    if total >= 100 and player_turn:
        print("\nPlayer win the game")
        running = False

    elif total >= 100 and not player_turn:
        print("\nComputer win the game")
        running = False
