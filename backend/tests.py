import pytest
from click.testing import CliRunner
from app import calculator, cli


def test_add():
    assert calculator("2+2.0") == 4.0
    assert calculator(".2 + 2.0") == 2.2


def test_subtract():
    assert calculator(" 2-2") == 0
    assert round(calculator(".1-.4"), 2) == -0.3


def test_multiply():
    assert calculator("2* 2") == 4
    assert round(calculator("0.2 * 0.2"), 3) == 0.04


def test_divide():
    assert calculator("2/2") == 1


def test_multilple_operations():
    assert calculator("-.2+0.2") == 0
    assert calculator("12-2+4/3*6") == 18.0


def test_zero_division():
    assert calculator("2/0") == "E: Zero Division"


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, input="3+8*6/3-1")
    assert result.exit_code == 0
    assert result.output == "Arithmetic expression: 3+8*6/3-1\nAnswer: 18.0\n"


def test_cli_with_args():
    runner = CliRunner()
    result = runner.invoke(cli, ["--expr", "8*6/3.0-1"])
    assert result.exit_code == 0
    assert result.output == "Answer: 15.0\n"


def test_cli_with_errors():
    runner = CliRunner()
    result = runner.invoke(cli, ["--expr", "5-1*6/2+"])
    assert result.exit_code == 0
    assert result.output == "Answer: E: Malformed Expression, see --help\n"


@pytest.fixture
def app():
    from app import app
    app.config["TESTING"] = True
    return app


def test_api(app):
    test_client = app.test_client()
    response = test_client.post("/api")
    expected_json = {"msg": "Missing JSON in request"}
    assert response.status_code == 400
    assert response.get_json() == expected_json


def test_api_missing_values(app):
    data = {"number1": "20", "number2": "10"}
    test_client = app.test_client()
    response = test_client.post("/api", json=data)
    expected_json = {"msg": "Missing values"}
    assert response.status_code == 400
    assert response.get_json() == expected_json


def test_api_addition(app):
    data = {"number1": "20", "number2": "10", "operator": "+"}
    test_client = app.test_client()
    response = test_client.post("/api", json=data)
    expected_json = {"msg": "30.0"}
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_api_zero_division(app):
    data = {"number1": "3.1415926", "number2": "0", "operator": "/"}
    test_client = app.test_client()
    response = test_client.post("/api", json=data)
    expected_json = {"msg": "E: Zero Division"}
    assert response.status_code == 200
    assert response.get_json() == expected_json
