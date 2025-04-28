from flask import Flask, url_for,redirect
from app.lib import biblioteca_header, biblioteca_lituania


api = Flask(__name__)
@api.route("/", methods=['GET'])
def home() -> str:
    # Redirecționează automat către /lituania
    return redirect(url_for('index'))

@api.route("/lituania", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_lituania.descriere_lituania()
    return text

@api.route("/lituania/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_lituania.capitala_lituania()
    return text

@api.route("/lituania/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_lituania.steag_lituania()
    return text

