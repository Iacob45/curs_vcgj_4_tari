import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_spania


api = Flask(__name__)

@api.route("/spania", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_spania.descriere_spania()
    return text

@api.route("/spania/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_spania.capitala_spania()
    return text

@api.route("/spania/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_spania.steag_spania()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))

