from flask import Flask, url_for,redirect
from app.lib import biblioteca_header, biblioteca_CoreeaDeNord


api = Flask(__name__)
@api.route("/", methods=['GET'])
def home() -> str:
    return redirect(url_for('index'))

@api.route("/CoreeaDeNord", methods=['GET'])
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_CoreeaDeNord.descriere_CoreeaDeNord()
    return text

@api.route("/CoreeaDeNord/capitala", methods=['GET'])
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_CoreeaDeNord.capitala_CoreeaDeNord()
    return text

@api.route("/CoreeaDeNord/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_CoreeaDeNord.steag_CoreeaDeNord()
    return text

