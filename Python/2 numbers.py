#simple common functions for number
my_num = 639566729169
print(str(my_num)) #converting int to string
print(-22.0215)
print((3 * (4 + 5.4)) / 5 - 2) #can use arithemtic and PEMDAS
print(10 % 4) #modulus operator, divides but shows only remainder, should show 2
print(abs(-22)) #absolute value
print(pow(22,2)) #number, raised to the power of, should be 484
print(max(5,100)) #shows the highest number
print(min(5,100)) #shows the lowest number
print(round(3.2)) #rounds off number
print(2**3) # == 2^3, exponential function

#some math functions need import from Python math
from math import * #called a math module
print(floor(4.7)) #round down
print(ceil(4.3)) #round up
print(sqrt(100)) #square root

#storing number input into variables
num1 = input("Enter a integer: ")
num2 = input("Enter a decimal: ")
result = int(num1) + float(num2) #int to integer, float to decimal
print(result)




