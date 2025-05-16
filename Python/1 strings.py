print("Hello World")

#variables can store strings, numbers, and boolean value
name = "Ky" #storing string
age = 22 #storing number
is_pretty = True #storing boolean value
print("My name is " + name + "! I am your programmer.") #print("string" + var) -> concatanation
print(f"My name is {name}! I am your programmer") # f string: shorter version of concatanation

print("I am " + str(age) + " years old. I'm pretty young")
#changing what is stored in a variable is possible
name = "Robin"
print("I named my laptop " + name + ". You are " + name + ".")

#You cannot put random indentations

#use \n to enter what's next of the string to the next line
print("Love,\nKy")
#use backlash \ to print a quotation mark
print("\"The Programmer\"")

#simple common functions for strings
phrase = "This is a PHRASE"
print(phrase.lower()) #function that convert string to lower case
print(phrase.lower().islower()) #should be true, .islower checks if string is in lowercase
print(phrase.upper()) #function that convert string to upper case
print(phrase.upper().islower()) #should be false
print(len(phrase)) #shows how many characters (len = length)
print(phrase[0]) #grabs nth letter from string, STRING INDEX STARTS AT 0, should show T
print(phrase.index("T")) #passing a parameter??, inverse of top function, should show 0
print(phrase.index("PHRASE")) #gives a value where "p" started
print(phrase.replace("PHRASE", "sentence.")) #replaces a part of the string to a new input

#storing string input into variables
name = input("Enter your name: ")
age = input("Enter your age: ") #stores a string value
print("Hello " + name + "! You are " + age + " years old.")

#madlibs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color + ",")
print(plural_noun + " are blue,")
print("I love " + celebrity + ".")
