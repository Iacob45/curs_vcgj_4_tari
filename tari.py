import sys
from flask import Flask
from app.lib import biblioteca_spania

api = Flask(__name__)

@api.route("/spania", methods=['GET'])
def index() -> str:
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #ffe6e6;
                color: #001f3f;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 40px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                margin: 10px;
                background-color: white;
                border: 2px solid #001f3f;
                color: #001f3f;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <a href="/spania/capitala"><button>Capitala</button></a>
        <a href="/spania/steag"><button>Steag</button></a>
        <h1>Aceasta este descrierea Spaniei</h1>
        <br>
        """ + biblioteca_spania.descriere_spania() + """
    </body>
    </html>
    """

@api.route("/spania/capitala", methods=['GET'])
def capitala() -> str:
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #ffe6e6;
                color: #001f3f;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 40px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                margin: 10px;
                background-color: white;
                border: 2px solid #001f3f;
                color: #001f3f;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <a href="/spania"><button>Descriere</button></a>
        <a href="/spania/steag"><button>Steag</button></a>
        <h1>Aceasta este capitala Spaniei</h1>
        <br>
        """ + biblioteca_spania.capitala_spania() + """
    </body>
    </html>
    """

@api.route("/spania/steag", methods=['GET'])
def steag() -> str:
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #ffe6e6;
                color: #001f3f;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 40px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                margin: 10px;
                background-color: white;
                border: 2px solid #001f3f;
                color: #001f3f;
                border-radius: 4px;
            }
            img {
                max-width: 600px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <a href="/spania"><button>Descriere</button></a>
        <a href="/spania/capitala"><button>Capitala</button></a>
        <h1>Acesta este steagul Spaniei</h1>
        <br>
        """ + biblioteca_spania.steag_spania() + """
    </body>
    </html>
    """

@api.cli.command()
def test():
    """
    Rulare 'unit tests'
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))

