from flask import Flask, url_for
from app.lib import biblioteca_grecia
from app.lib.biblioteca_grecia import descriere_grecia, capitala_grecia, steag_grecia
api = Flask(__name__)

@api.route("/grecia", methods=['GET'])
def index() -> str:
    return descriere_grecia()



@api.route("/grecia/capitala", methods=['GET'])
def capitala() -> str:
    return capitala_grecia()

@api.route("/grecia/steag", methods=['GET'])
def steag() -> str:
    return steag_grecia()

