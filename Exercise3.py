num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operation = input("Do you want to add, subtract, multiply or divide? ")

if operation == "add":
    print(num1 + num2)
elif operation == "subtract":
    print(num1 - num2)
elif operation == "multiply":
    print(num1 * num2)
elif operation == "divide":
    print(num1 / num2)
else:
    print("That's not a valid operation")