import sys
from flask import Flask, url_for
from app.lib import biblioteca_brazilia

api = Flask(__name__)


@api.route("/brazilia", methods=['GET'])
def index() -> str:
    return biblioteca_brazilia.descriere_brazilia()


@api.route("/brazilia/capitala", methods=['GET'])
def capitala() -> str:
    return biblioteca_brazilia.capitala_brazilia()


@api.route("/brazilia/steag", methods=['GET'])
def steag() -> str:
    return biblioteca_brazilia.steag_brazilia()


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))


