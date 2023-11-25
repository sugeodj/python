# calculator that can calculate addition, subtraction, multiplication, and division from terminal input

# import sys module
import sys


# define function to add two numbers
def add(x, y):
    return x + y


# define function to subtract two numbers
def subtract(x, y):
    return x - y


# define function to multiply two numbers
def multiply(x, y):
    return x * y


# define function to divide two numbers
def divide(x, y):
    return x / y


while True:
    # prompt input of numbers and operator
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # take input from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):
        # if choice is 5, exit program
        if choice == '5':
            print("Exiting calculator...")
            sys.exit()

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # if choice is 1, add the two numbers
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        # if choice is 2, subtract the two numbers
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        # if choice is 3, multiply the two numbers
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        # if choice is 4, divide the two numbers
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
    else:
        # if choice is not one of the five options, print error message
        print("Invalid input.")
