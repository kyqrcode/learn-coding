# if statement = condition need to meet to do action
# use elif statement if you need to disregard other if statements
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif is_tall and not(is_male):
    print("you are not a male but are tall")
else:
    print("You are neither male nor tall")


# if statements with comparison
def max_num(num1, num2, num3): # can also be used for strings and booleans
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5)) 
