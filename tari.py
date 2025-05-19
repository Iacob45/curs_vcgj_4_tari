from flask import Flask, url_for,redirect
from app.lib import biblioteca_header, biblioteca_egipt
import sys

api = Flask(__name__)
@api.route("/", methods=['GET'])
def home() -> str:

    return redirect(url_for('index'))

@api.route("/egipt", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_egipt.descriere_egipt()
    return text

@api.route("/egipt/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_egipt.capitala_egipt()
    return text

@api.route("/egipt/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_egipt.steag_egipt()
    return text


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))
