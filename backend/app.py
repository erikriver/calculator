from operator import add, sub, mul, truediv

operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculator(string):
    """
    Recursive function that allows operations with more than two numbers
    in string formant.
    """
    try:
        # Parse negative numbers and clean spaces
        return float(string)
    except ValueError:
        pass

    for c in operators.keys():
        left, operator, right = string.partition(c)
        if operator in operators:
            return operators[operator](calculator(left), calculator(right))


if __name__ == "__main__":
    calc = input("Expression:\n")
    print("Answer: " + str(calculator(calc)))
