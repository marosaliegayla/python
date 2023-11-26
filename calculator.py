def calculator():
     while True:
        print("Hello, Welcome to my Calculator! by Rosalie")
        input("Press Enter to continue...")
    
        num1 = int(input("What is the first number?"))
        num2 = int(input("What is the second number?"))
        operation = input("What do you want to do with it? \n 1. add \n 2. subtract \n 3. divide \n 4. multiply \n 5. nothing \n ")
    
        if (operation == 'Add') or (operation == 'add') or (operation == '1'):
            print(num1 + num2)
        elif (operation == 'Subtract') or (operation == 'subtract') or (operation == '2'):
            print(num1 - num2)
        elif (operation == 'Multiply') or (operation == 'multiply') or (operation == '3'):
            print(num1 * num2)
        elif (operation == 'Divide') or (operation == 'divide') or (operation == '4'):
            print(num1 / num2)
        elif (operation == 'Nothing') or (operation == 'nothing') or (operation == '5'):
            print("Okay then, touch some grass")
        else:
            print("I don't understand")

        exit_choice = input("Do you want to exit? (yes/no): ")
        if exit_choice.lower() == 'yes':
            break

calculator()
