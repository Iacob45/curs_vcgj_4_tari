import sys
import pytest
from flask import Flask
from app.lib.biblioteca_vatican import descriere_vatican, capitala_vatican, steag_vatican

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru CANADA (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/vatican", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Canadei."""
    return descriere_vatican()

@api.route("/vatican/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Canadei."""
    return capitala_vatican()


@api.route("/vatican/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Canadei."""
    return steag_vatican()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))


if __name__ == "__main__":
    api.run(debug=True)