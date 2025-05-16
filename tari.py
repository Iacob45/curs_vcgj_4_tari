import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_germania


api = Flask(__name__)

@api.route("/germania", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_germania.descriere_germania()
    return text

@api.route("/germania/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_germania.capitala_germania()
    return text

@api.route("/germania/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_germania.steag_germania()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))