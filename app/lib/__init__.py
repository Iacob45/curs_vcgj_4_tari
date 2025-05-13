from flask import Flask

# Crearea aplicației Flask
app = Flask(__name__)

# Importarea altor fișiere care conțin rute, configurări, etc.
from app import routes

