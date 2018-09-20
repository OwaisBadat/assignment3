#calculator

from calculator import multiplication,division,addition,subtraction


while True:

    try:
        first_number = int(input("Input your first number: "))
        second_number = int(input("Input your second number: "))


        operand = input("Would you like to +, -, *, /:")
        if (operand != "+" or operand != "-" or operand != "*" or operand != "/"):
            print("Please input an operand from the provided list of functions")

        if operand == "*":
            results = multiplication(first_number,second_number)
        elif operand == "/":
            results = division(first_number,second_number)
        elif operand == "+":
            results = addition(first_number,second_number)
        elif operand == "-":
            results = subtraction(first_number,second_number)

        print(results)

        user_quit = input("Please press 'q' if you are ready to exit:")
        if(user_quit == "q"):
            print("Thank you for using Owais's calculator")
            break

    except ValueError:
        print("Please input numbers only")
