import math

def calculate(num1, operator, num2=None): 
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ZeroDivisionError("Can't divide by zero")
        case '^':
            return num1 ** num2
        case '√':
            return math.sqrt(num1)
        case '%':
            return num1 % num2
        case _:
            raise ValueError("Invalid operator! Please use: +, -, *, /, ^, √, %")