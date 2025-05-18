import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_andorra


api = Flask(__name__)

@api.route("/andorra", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_andorra.descriere_andorra()
    return text

@api.route("/andorra/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_andorra.capitala_andorra()
    return text

@api.route("/andorra/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_andorra.steag_andorra()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))

