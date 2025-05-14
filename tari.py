import sys
import pytest
from flask import Flask
from app.lib.biblioteca_danemarca import descriere_danemarca, capitala_danemarca, steag_danemarca

""" Modulul `tari.py` conține funcții care generează pagini HTML pentru DANEMARCA (descriere, capitală, steag). """
api = Flask(__name__)


@api.route("/danemarca", methods=['GET'])
def index() -> str:
    """Returnează HTML-ul cu descrierea Danemarcei."""
    return descriere_danemarca()

@api.route("/danemarca/capitala", methods=['GET'])
def capitala() -> str:
    """Returnează HTML-ul capitala Danemarcei."""
    return capitala_danemarca()


@api.route("/danemarca/steag", methods=['GET'])
def steag() -> str:
    """Returnează HTML-ul cu drapelul Danemarcei."""
    return steag_danemarca()

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    sys.exit(pytest.main(["."]))
