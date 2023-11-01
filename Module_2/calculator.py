result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("Enter a number, operator or '=' to calculate: ")

    # Якщо користувач ввів число
    if user_input.isdigit() or '.' in user_input:
        if wait_for_number:
            operand = float(user_input)
            if result is None:
                result = operand
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        print("Error: Division by zero. Enter another number.")
                        continue
                    result /= operand
            wait_for_number = False
        else:
            print("Error: Expected an operator. Please enter an operator.")
            continue

    # Якщо користувач ввів оператор
    elif user_input in ['+', '-', '*', '/']:
        if not wait_for_number:
            operator = user_input
            wait_for_number = True
        else:
            print("Error: Expected a number. Please enter a number.")
            continue

    # Якщо користувач ввів '='
    elif user_input == '=':
        print("Result:", result)
        break

    # Якщо користувач ввів щось інше
    else:
        print("Error: Invalid input. Please enter a valid number or operator.")
