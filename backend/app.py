import click
from operator import add, sub, mul, truediv

operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculator(string):
    """
    Recursive function that allows operations with more than two numbers
    and different operators in string formant.
    """
    try:
        # Parse negative numbers and clean spaces
        return float(string)
    except ValueError:
        pass

    for c in operators.keys():
        left, op, right = string.partition(c)
        if op in operators:
            try:
                answer = operators[op](calculator(left), calculator(right))
            except ZeroDivisionError:
                answer = "E: Zero Division"
            except TypeError:
                answer = "E: Malformed Expression, see --help"
            finally:
                return answer


@click.command()
@click.option(
    "--expr",
    prompt="Arithmetic expression",
    help="The expression that you want to evaluate with operatos such as +, -, *, / \n"  # noqa: E501
    "and expressions are like 2*3+2,  3.5-1.5, -20/5",
)
def cli(expr):
    answer = calculator(expr)
    print("Answer: " + str(answer))


if __name__ == "__main__":
    cli()
