# A calculator app

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."


def calculator():
    print("Simple Calculator")
    print("Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

choice = input("Enter the number of your desired operation (1-4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    else:
        result = divide(num1, num2)
        operation = '/'

    print(f"{num1} {operation} {num2} = {result}")

else:
    print("Invalid choice. Please enter a number between 1 and 4.")

# Run code

calculator()

