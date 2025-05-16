import random

print("Play rock, paper, scissors with me! (WARNING: Case sensitive)")

def play():
    player_hand = input("Pick your hand: rock, paper, scissors\n")

    hand = ["rock", "paper", "scissors"]
    computer_hand = random.choice(hand)

    battle = {
        "player": player_hand,
        "computer": computer_hand
    }
    return battle

battle = play()
print(f'You chose {battle["player"]}, Computer chose {battle["computer"]}')

def check_win(player, computer):
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, you lose!"
        elif computer == "scissors":
            return "You win!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        elif computer == "scissors":
            return "Scissors cuts paper, you lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        elif computer == "rock":
            return "Rock smashes scissors, you lose!"
    else:
        return "What's a " + player + "?"

result = check_win(battle["player"], battle["computer"])
print(result)