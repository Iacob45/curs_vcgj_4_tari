import sys
from flask import Flask
from app.lib.biblioteca_vatican import descriere_vatican, capitala_vatican, steag_vatican

""" Modulul tari.py conține funcții care generează pagini HTML pentru VATICAN (descriere, capitala, steag). """
api = Flask(__name__)


@api.route("/vatican", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Vaticanului."""
    return descriere_vatican()


@api.route("/vatican/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Vaticanului."""
    return capitala_vatican()


@api.route("/vatican/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Vaticanului."""
    return steag_vatican()


@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))

