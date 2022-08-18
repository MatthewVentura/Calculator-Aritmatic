# First 4 functions initialize the instructions for running the operation
def add():
  x = int(input("Enter a number: "))
  y = int(input("Enter a number: "))
  result = x + y 
  return result
# Function known as "Subtract" takes x and y from input and stores it in the variable
def subtract():
  x = int(input("Enter a number: "))
  y = int(input("Enter a another number: "))
  result = x - y
  return result
# same thing occurs here
def divide():
  x = int(input("Enter a number: "))
  y = int(input("Enter a number: "))
  result = x / y
  return result
# Same thing here 
def multiply():
  x = int(input("Enter a number: "))
  y = int(input('Enter a number: '))
  result = x * y
  return result


quit = False

while (not quit):
    print('Welcome to your calculator!!!')
    print()

    # takes the user input and stores it in the operand 
    operand = input("Choose an operation: \n + \n - \n * \n / \n Q\n")
    # makes a new line to display each operand 

    # uses conditionals to see what operation the user picks 
    if operand == "+":
        print(add())
    elif operand == "-":
        print(subtract())
    elif operand == "/":
        print(divide())
    elif operand == "Q":
        quit = True
    else:
        print(multiply())
