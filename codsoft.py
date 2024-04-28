# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Prompting the user for input
while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    operator = input("Enter operator (+, -, *, /): ")
    if operator in ('+', '-', '*', '/'):
        break
    else:
        print("Invalid operator! Please enter +, -, *, or /.")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Perform the calculation based on the user's choice of operator
if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
