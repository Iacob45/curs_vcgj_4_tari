import sys
import pytest
from flask import Flask
from app.lib.biblioteca_japonia import descriere_japonia, capitala_japonia, steag_japonia

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru JAPONIA (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/japonia", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Japoniei."""
    return descriere_japonia()

@api.route("/japonia/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Japoniei."""
    return capitala_japonia()


@api.route("/japonia/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Japoniei."""
    return steag_japonia()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))
