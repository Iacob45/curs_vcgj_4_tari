import sys
from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_guatemala

api = Flask(__name__)

@api.route("/guatemala", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_guatemala.descriere_guatemala()
    return text

@api.route("/guatemala/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_guatemala.capitala_guatemala()
    return text

@api.route("/guatemala/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_guatemala.steag_guatemala()

    return text

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))