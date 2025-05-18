"""Aplicație Flask care afișează descrierea, capitala și steagul Franței."""

import sys
import pytest  # import mutat sus
from flask import Flask
from app.lib import biblioteca_franta

api = Flask(__name__)


@api.route("/franta", methods=['GET'])
def index() -> str:
    """Afișează descrierea Franței împreună cu headerul HTML."""
    text = biblioteca_franta.header_descriere()
    text += biblioteca_franta.descriere_franta()
    return text


@api.route("/franta/capitala", methods=['GET'])
def capitala() -> str:
    """Afișează pagina cu informații despre capitala Franței."""
    text = biblioteca_franta.header_capitala()
    text += biblioteca_franta.capitala_franta()
    return text


@api.route("/franta/steag", methods=['GET'])
def steag() -> str:
    """Afișează pagina cu imaginea steagului Franței."""
    text = biblioteca_franta.header_steag()
    text += biblioteca_franta.steag_franta()
    return text


@api.cli.command()
def test():
    """Rulează testele unitare folosind pytest."""
    sys.exit(pytest.main(["."]))
