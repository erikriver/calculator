import click
from flask import Flask, request, jsonify
from operator import add, sub, mul, truediv

app = Flask(__name__, static_folder="./client", static_url_path="/")
operators = {"+": add, "-": sub, "x": mul, "/": truediv}


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api", methods=["POST"])
def api():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    number1 = request.json.get("number1")
    number2 = request.json.get("number2")
    operator = request.json.get("operator")

    if not number1 or not number2 or not operator:
        return jsonify({"msg": "Missing values"}), 400

    expression = str(number1) + operator + str(number2)
    answer = calculator(expression)
    return jsonify({"msg": str(answer)}), 200


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
    help="The expression that you want to evaluate with operatos such as +, -, x, / \n"  # noqa: E501
    "and expressions are like 2x3+2,  3.5-1.5, -20/5",
)
def cli(expr):
    answer = calculator(expr)
    print("Answer: " + str(answer))


if __name__ == "__main__":
    cli()
