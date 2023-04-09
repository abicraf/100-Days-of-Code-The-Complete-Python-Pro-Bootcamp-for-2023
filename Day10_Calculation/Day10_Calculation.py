from art import logo
from replit import clear

def add(n1,n2):
    """adding ++ number"""
    return n1+n2

def substract(n1,n2):
    """substract -- number"""
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiple,
    "/": devide,
}

print(logo)
def calculator_function():
    continue_flag = 'y'
    num_1 = float(input("What's the first number? "))

    for n in operations:
        print(n)
    while continue_flag == 'y':
        symbol = input("Pick an opreation from the line above: ")
        num_2 = float(input("What's the next number? "))

        calculation = operations[symbol]
        answer = calculation(num_1, num_2)
        print(f"{num_1} {symbol} {num_2} = {answer}")
        continue_flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over again.: ")
        num_1 = answer
        if continue_flag == 'n':
            clear()
            calculator_function()


calculator_function()
