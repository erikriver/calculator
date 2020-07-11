def calculator(num1, num2, operator):
    out = None

    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2
    return out


if __name__ == "__main__":
    num1 = input("First Number:\n")
    operator = input("Operator (+, -, *, /):\n")
    num2 = input("Second Number:\n")

    num1 = float(num1)
    num2 = float(num2)

    answer = calculator(num1, num2, operator)

    print("Answer: " + str(answer))
