import operations

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power (x^y)")
print("6. Square Root")
print("7. Modulo")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '7'): # Operations requiring two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {operations.add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {operations.subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {operations.multiply(num1, num2)}")
        elif choice == '4':
            result = operations.divide(num1, num2)
            if isinstance(result, str):
                 print(result)
            else:
                 print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {operations.power(num1, num2)}")
        elif choice == '7':
             result = operations.modulo(num1, num2)
             if isinstance(result, str):
                 print(result)
             else:
                 print(f"{num1} % {num2} = {result}")

    elif choice == '6': # Square root only needs one number
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        result = operations.square_root(num)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Square root of {num} = {result}")

    else:
        print("Invalid Input")
        continue # Go to next iteration if input is invalid

    # Check if the user wants another calculation
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()
        if next_calculation == 'yes':
            break # Continue with the main loop
        elif next_calculation == 'no':
            break # Exit the main loop
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
    if next_calculation == 'no':
        break 