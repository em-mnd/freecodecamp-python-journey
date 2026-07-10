from main_logic import add, substract as sub, multiply as mul, divide as div

first_number = int(input("Enter the first number: "))
if first_number != int:
    print("Please enter a valid number.")

second_number = int(input("Enter the second number: "))
if second_number != int:
    print("Please enter a valid number.")

operation = input("Enter the operation (add, sub, mul, div): ")

if operation not in ["add", "sub", "mul", "div"]:
    print("Invalid operation. Please choose from add, sub, mul, or div.")
elif operation == "add":
    result = add(first_number, second_number)
elif operation == "sub":
    result = sub(first_number, second_number)
elif operation == "mul":
    result = mul(first_number, second_number)
elif operation == "div":
    if second_number == 0:
        print("Cannot divide by zero.")
        second_number = int(input("Choose a different second number: "))
        if second_number == 0:
            print("Invalid input. Cannot divide by zero.")
        else:
            result = div(first_number, second_number)
    else:
        result = div(first_number, second_number)
else:
    print(f"Result: {result}")