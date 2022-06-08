def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def division(number1, number2):
    return number1 / number2


def multiplication(number1, number2):
    return number1 * number2


def modulus(number1, number2):
    return number1 % number2


while True:
    print("What operation would you like to perform today? \n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Division\n"
          "4. Multiplication\n"
          "5. Modulus\n")

    answer = int(input("Select from 1, 2, 3, 4, 5 : "))

    if answer in (1, 2, 3, 4, 5):
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        if answer == 1:
            print(first_number, "+", second_number, "=",
                  addition(first_number, second_number))

        elif answer == 2:
            print(first_number, "-", second_number, "=",
                  subtraction(first_number, second_number))

        elif answer == 3:
            print(first_number, "/", second_number, "=",
                  division(first_number, second_number))

        elif answer == 4:
            print(first_number, "*", second_number, "=",
                  multiplication(first_number, second_number))

        elif answer == 5:
            print(first_number, "%", second_number, "=",
                  modulus(first_number, second_number))

    else:
        print("Invalid input")

    choice = input("Would you like to truy another operation? [y, n] ")
    if choice == 'y':
        continue
    if choice == 'n':
        break

# Press CTRL + C to quit the loop
