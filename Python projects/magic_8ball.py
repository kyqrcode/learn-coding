import random

name = input("Tell me your name.\n")

print("Hello " + name + ". Ask me about your future, and may the universe be kind to enough to show me a glimpse of your tomorrow. Howver, the answer you seek may only be in the form of yes or no")

question = input("What is your question?\n")
answer = ""

if question == "":
    print("No questions asked, please ask me a question")
else:
    random_num = random.randint(1,9)

    if random_num == 1:
        print("Yes - definetly")
    elif random_num == 2:
        print("It is decidedly so")
    elif random_num == 3:
        print("Without a doubt")
    elif random_num == 4:
        print("Question hazy - try again")
    elif random_num == 5:
        print("Better not tell you now")
    elif random_num == 6:
        print("The universe does not want you to know for now")
    elif random_num == 7:
        print("I don't think so")
    elif random_num == 8:
        print("Very doubtful")
    elif random_num == 9:
        print("A resounding no")
    else:
        print("Error!")
    