def e(phrase):
    a_letter = ""
    for letter in phrase:
        if letter.lower() in "aiou":
            if letter.isupper():
                a_letter = a_letter + "E"
            else:
                a_letter = a_letter + "e" 
        else:
            a_letter = a_letter + letter
    return a_letter

print(e(input("Enter a phrase: ")))