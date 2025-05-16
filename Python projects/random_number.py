import random

try:
  print("Welcome to the Number Generator")
  gen_num = input("Generate a new random number? (y/n) \n")
  if gen_num == "y":
    while gen_num == "y":
      num_list = range(1, 11)
      print(random.choice(num_list))
      gen_num = input("Generate a new random number? (y/n) \n")
  if gen_num == "n":
    print("Have a nice day!")
  else:
    raise Exception("Error! Please input y or n.")
except Exception as error:
  print(error)