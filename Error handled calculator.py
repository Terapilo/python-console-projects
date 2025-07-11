while True:
    print("\n===CALCULATOR===")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")
    choice = input("Choose an operation (1-5)").strip()
    if choice=="5":
        print("Exiting calcultor")
    if choice not in["1", "2", "3", "4", "5"]:
        print("Invalid option. please select from 1 to 5")
        continue
    try:
        num1 = float(input("Please enter first number"))
        num2 = float(input("Please enter second number"))
    except ValueError:
        print("Please enter a valid number")
        continue
    try:
        if choice == "1":
            result = num1+num2
            operation="+"
        elif choice == "2":
            result = num1-num2
            operation = "-"
        elif choice == "3":
            reult = num1*num2
            operation = "X"
        elif choice == "4":
            result = num1/num2
            operation = "/"
        print(f"{num1} {operation} {num2} = {result}")
    except ZeroDivisionError:
        print("Please enter a number")


