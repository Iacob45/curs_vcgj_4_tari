import sys
import pytest
from flask import Flask
from app.lib.biblioteca_canada import descriere_canada, capitala_canada, steag_canada

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru diverse țări (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/canada", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Canadei."""
    return descriere_canada()

@api.route("/canada/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Canadei."""
    return capitala_canada()


@api.route("/canada/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Canadei."""
    return steag_canada()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))
