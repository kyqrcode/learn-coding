num1 = float(input("Enter first number: ")) #can use float or int for input
op = input("Enter arithmethic operator (+, -, *, /, ^): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "^":
    print(num1 ** num2)
else:
    print("Invalid operator")