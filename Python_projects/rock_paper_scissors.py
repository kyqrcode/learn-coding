import random

print("Play rock, paper scissors with me!")
user_hand = int(input("Pick: (1) Rock, (2) Paper, (3) Scissors\n"))

while user_hand < 1 or user_hand > 3:
    user_hand = int(input("Please pick between the valid choices: "))

print("Rock, paper, scissors, SHOOT!")
comp_hand = random.randint(1,3)

if user_hand == comp_hand:
    print("It's a draw!")
elif user_hand == 1:
    if comp_hand == 2:
        print("Rock vs Paper! You Lose!") 
    if comp_hand == 3:
        print("Rock vs Scissors! You win!")
elif user_hand == 2:
    if comp_hand == 1:
        print("Paper vs Rock! You win!") 
    if comp_hand == 3:
        print("Paper vs Scissors! You lose!")
elif user_hand == 3:
    if comp_hand == 1:
        print("Scissors vs Rock! You lose!") 
    if comp_hand == 2:
        print("Scissors vs Paper! You win!")
else:
    print("Invalid hand")
