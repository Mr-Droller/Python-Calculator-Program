start = 'p'
while (start != 's'):
    start = input("Input s to start the calculator: ")

while (start == 's'):
    num1 = float(input("Enter a number 1: "))
    num2 = float(input("Enter a number 2: "))

    operation = input("Choose an operation +, -, *, /: ")

    if (operation == "+"):
        result = num1 + num2
        print(f"The result is {result}")
    elif (operation == "-"):
        result = num1 - num2
        print(f"The result is {result}")
    elif (operation == "*"):
        result = num1 * num2
        print(f"The result is {result}")
    elif (operation == "/"):
        if num2 == 0:
            print("Cannot divide by Zero")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    else:
        print("Invalid Operation")

    start = input("Do you want to stop? (Press q) else input s")
