import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_kosovo


api = Flask(__name__)

@api.route("/kosovo", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_kosovo.descriere_kosovo()
    return text

@api.route("/kosovo/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_kosovo.capitala_kosovo()
    return text

@api.route("/kosovo/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_kosovo.steag_kosovo()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))

