from flask import Flask, render_template
from app.lib import biblioteca_header, biblioteca_bulgaria

api = Flask(__name__)

@api.route("/", methods=['GET'])
def index() -> str:
    return render_template(
        "index.html", 
        header_descriere=biblioteca_header.header_descriere(),
        descriere=biblioteca_bulgaria.descriere_bulgaria()
    )

@api.route("/capitala", methods=['GET'])
def capitala() -> str:
    return render_template(
        "capitala.html", 
        header_capitala=biblioteca_header.header_capitala(),
        capitala=biblioteca_bulgaria.capitala_bulgaria()
    )

@api.route("/steag", methods=['GET'])
def steag() -> str:
    return render_template(
        "steag.html", 
        header_steag=biblioteca_header.header_steag(),
        steag=biblioteca_bulgaria.steag_bulgaria()
    )

if __name__ == "__main__":
    api.run(debug=True, port=5011)
