from main_logic import add, substract as sub, multiply as mul, divide as div

first_number = float(input("Enter the first number: "))
if first_number != float or first_number != int:
    print("Please enter a valid number.")

second_number = float(input("Enter the second number: "))
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
        second_number = float(input("Choose a different second number: "))
        while second_number == 0:
            print("Invalid input. Cannot divide by zero.")
            second_number = float(input("Choose a different second number: "))
            if second_number == 0 or second_number != "":
                print("Please enter a valid number.")
        result = div(first_number, second_number)
print(f"Result: {result}")