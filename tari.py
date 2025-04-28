import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_romania


api = Flask(__name__)

@api.route("/romania", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_romania.descriere_romania()
    return text

@api.route("/romania/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_romania.capitala_romania()
    return text

@api.route("/romania/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_romania.steag_romania()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))

