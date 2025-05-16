#Try/Except
try:
    num = float(input("Enter a number: "))
    print("Thank you for inputing a number")

#try exception alone is very vague
except ValueError: #best with specified errors like "ValueError" (may also catch division by zero, etc)
    print("Invalid Input: That is not a number!")

#another example of a specified error:
except ZeroDivisionError:
    print("Cannot be divideed by 0")

else:
    #no exceptions were raised, the code ran successfully
    print("yay")

finally:
    #do something in any case
    print("okay")


try:
    raise Exception("An error!") #raises an error even if there's no error
except Exception as error:
    print(error)