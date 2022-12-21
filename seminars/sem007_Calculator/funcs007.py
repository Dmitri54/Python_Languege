
def do_it(symbol):
    num1, num2, op = symbol
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '*':
        return int(num1) * int(num2)
    elif op == '/':
        return int(num1) / int(num2)
