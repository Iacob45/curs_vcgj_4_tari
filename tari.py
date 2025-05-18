import sys
import pytest
from flask import Flask
from app.lib.biblioteca_italia import descriere_italia, capitala_italia, steag_italia

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru ITALIA (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/italia", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Italiei."""
    return descriere_italia()

@api.route("/italia/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Italia."""
    return capitala_italia()


@api.route("/italia/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Italiei."""
    return steag_italia()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))
