import sys
from flask import Flask, url_for, send_from_directory
from app.lib import biblioteca_header, biblioteca_Luxembourg


api = Flask(__name__)

@api.route("/luxembourg", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_Luxembourg.descriere_luxembourg()
    return text

@api.route("/luxembourg/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_Luxembourg.capitala_luxembourg()
    return text

@api.route("/luxembourg/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_Luxembourg.steag_luxembourg()
    return text

@api.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@api.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest
    sys.exit(pytest.main(["."]))

