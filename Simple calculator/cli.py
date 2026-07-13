from main_logic import add, substract as sub, multiply as mul, divide as div


first_number = float(input("Enter the first number: "))
if first_number != float:
    print("Please enter a valid number.")
else:
    print(f"First number is: {first_number}")

second_number = float(input("Enter the second number: "))
if second_number != float:
    print("Please enter a valid number.")
else:
    print(f"Second number is: {second_number}")

operation = input("Enter the operation (add, sub, mul, div): ")

if operation not in ["add", "sub", "mul", "div"].lower():
    print("Invalid operation. Please choose from add, sub, mul, or div.")
elif operation == "add":
    result = add(first_number, second_number)
elif operation == "sub":
    result = sub(first_number, second_number)
elif operation == "mul":
    result = mul(first_number, second_number)
elif operation == "div":
    try:
        result= div(first_number, second_number)
    except ValueError:
        print(ValueError)
    else:
        if second_number != 0:
            result = div(first_number, second_number)
            print(f"Result: {result}")

continue_operation = input("Do you want to continue the operation ?: (yes/no): ").lower()
if continue_operation == "no":
    print("Exiting the calculator. Goodbye!")
    exit()
elif continue_operation == 'yes':
    print("Continuing the operation.")