from flask import Flask, url_for
from app.lib import biblioteca_header, biblioteca_romania, biblioteca_germania, biblioteca_olanda, biblioteca_franta

api = Flask(__name__)

@api.route("/", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_romania.descriere_romania()
    text += biblioteca_germania.descriere_germania()
    text += biblioteca_olanda.descriere_olanda()
    text += biblioteca_franta.descriere_franta()
    return text

@api.route("/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_romania.capitala_romania()
    text += biblioteca_germania.capitala_germania()
    text += biblioteca_olanda.capitala_olanda()
    text += biblioteca_franta.capitala_franta()
    return text

@api.route("/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_romania.steag_romania()
    text += biblioteca_germania.steag_germania()
    text += biblioteca_olanda.steag_olanda()
    text += biblioteca_franta.steag_franta()
    return text
