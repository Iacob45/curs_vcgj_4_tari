import sys
import pytest
from flask import Flask
from app.lib.biblioteca_egipt import descriere_egipt, capitala_egipt, steag_egipt

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru EGIPT (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/egipt", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Egiptului."""
    return descriere_egipt()

@api.route("/egipt/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Egiptului."""
    return capitala_egipt()


@api.route("/egipt/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Egiptului."""
    return steag_egipt()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))
