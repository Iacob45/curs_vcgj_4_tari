from flask import Flask, render_template
from app.lib import biblioteca_header, biblioteca_olanda

api = Flask(__name__)

# Ruta pentru pagina principală (Descrierea Olandei)
@api.route("/", methods=['GET'])
def index() -> str:
    return render_template(
        "index.html", 
        header=biblioteca_header.header_descriere_olanda(),
        descriere=biblioteca_olanda.descriere_olanda()
    )

# Ruta pentru pagina cu capitala Olandei
@api.route("/olanda/capitala", methods=['GET'])
def capitala() -> str:
    return render_template(
        "capitala.html", 
        header=biblioteca_header.header_capitala_olanda(),
        capitala=biblioteca_olanda.capitala_olanda()
    )

# Ruta pentru pagina cu steagul Olandei
@api.route("/olanda/steag", methods=['GET'])
def steag() -> str:
    return render_template(
        "steag.html", 
        header=biblioteca_header.header_steag_olanda(),
        steag=biblioteca_olanda.steag_olanda()
    )

if __name__ == "__main__":
    api.run(debug=True, port=5011)
