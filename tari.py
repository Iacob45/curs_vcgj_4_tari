from flask import Flask, render_template
from app.lib import biblioteca_header, biblioteca_portugalia

api = Flask(__name__)

# Ruta pentru pagina principală (Descrierea Portugaliei)
@api.route("/", methods=['GET'])
def index() -> str:
    return render_template(
        "index.html", 
        header_descriere=biblioteca_header.header_descriere(),
        descriere=biblioteca_portugalia.descriere_portugalia()
    )

# Ruta pentru pagina cu capitala Portugaliei
@api.route("/capitala", methods=['GET'])
def capitala() -> str:
    return render_template(
        "capitala.html", 
        header_capitala=biblioteca_header.header_capitala(),
        capitala=biblioteca_portugalia.capitala_portugalia()
    )

# Ruta pentru pagina cu steagul Portugaliei
@api.route("/steag", methods=['GET'])
def steag() -> str:
    return render_template(
        "steag.html", 
        header_steag=biblioteca_header.header_steag(),
        steag=biblioteca_portugalia.steag_portugalia()
    )

if __name__ == "__main__":
    api.run(debug=True, port=5011)
