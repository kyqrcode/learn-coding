#guessing game with if statements and while loops
secret_word = "giraffe"
guess = input("You have 5 tries to guess the secret animal (clue: english, lowercase): ")
guess_count = 1
guess_limit = 5
lost_game = False

while guess != secret_word and not(lost_game):
    if guess_limit > guess_count:
        guess = input("Wrong! Guess again: ")
        guess_count += 1
    else:
        lost_game = True

if guess == secret_word:
    print("Congratulations! You got the secret word: giraffe")
else:
    print("You lose, try again next time!")