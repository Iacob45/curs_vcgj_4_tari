import sys
from flask import Flask, url_for
from app.lib.biblioteca_canada import descriere_canada, capitala_canada, steag_canada


api = Flask(__name__)


@api.route("/canada", methods=['GET'])
def index() -> str:
    return descriere_canada()

@api.route("/canada/capitala", methods=['GET'])
def capitala() -> str:
    return capitala_canada()


@api.route("/canada/steag", methods=['GET'])
def steag() -> str:
    return steag_canada()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))





