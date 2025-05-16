from flask import Flask
from app.lib.biblioteca_honduras import descriere_honduras, steag_honduras, capitala_honduras


api = Flask(__name__)

@api.route("/honduras", methods=['GET'])
def index():
    "Endpoint descriere"
    return descriere_honduras()

@api.route("/honduras/capitala", methods=['GET'])
def capitala():
    "Endpoint capitala"
    return capitala_honduras()

@api.route("/honduras/steag", methods=['GET'])
def steag():
    "Endpoint steag"
    return steag_honduras()
