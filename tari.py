from flask import Flask
from app.lib import biblioteca_header, biblioteca_olanda

api = Flask(__name__)

@api.route("/", methods=['GET'])
def index() -> str:
	text = biblioteca_header.header_descriere_olanda()
	text += biblioteca_olanda.descriere_olanda()

@api.route("/capitala", methods=['GET'])
def capitala() -> str:
    
    text = biblioteca_header.header_capitala_olanda()  
    text += biblioteca_olanda.capitala_olanda()  
    return text

@api.route("/steag", methods=['GET'])
def steag() -> str:
    text = biblioteca_header.header_steag_olanda()  
    text += biblioteca_olanda.steag_olanda()  
    return text
