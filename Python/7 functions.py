#function = collection of code that performs specific tasks
def trial(): #keyword for function
    print("Mid")
print("Top")

trial() #calling a function (for execution)

print("Bottom")
#indentations are crucial for an action to be included in the function
#print would be: Top \n Hello User \n Bottom


#parameter = information function receives
def say_hi(name): #parameter inside parenthesis
    print("Hello " + name + "!")

say_hi(input("Input you name: ")) #can put strings, numbers (covert to strings first), boolean

#return key word can return information from the function
def cube(num):
    return num * num * num #any function after return code will not be read

print(cube(3))