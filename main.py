from logo import logo

operations = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}

def calc():
    print(logo)
    should_accumulate = True
    first_number = float(input("What's the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number: "))
        answer = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

        if choice == 'y':
            first_number = answer
        else:
            should_accumulate = False
            print('\n' * 10)
            calc()


calc()