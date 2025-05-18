from flask import Flask, url_for
from app.lib import biblioteca_malta

api = Flask(__name__)

@api.route("/malta", methods=['GET'])
def index() -> str:
    return biblioteca_malta.descriere_malta()

@api.route("/malta/capitala", methods=['GET'])
def capitala() -> str:
    return biblioteca_malta.capitala_malta()

@api.route("/malta/steag", methods=['GET'])
def steag() -> str:
    return biblioteca_malta.steag_malta()
