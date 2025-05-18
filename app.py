from flask import Flask

app = Flask(__name__)

def descriere():
    return "<h1>Norvegia este o țară nordică cunoscută pentru fiorduri și peisaje montane.</h1>"

def capitala():
    return "<h1>Capitala Norvegiei este Oslo.</h1>"

def steag():
    return "<img src='https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Norway.svg' width='300'>"

@app.route('/Norvegia')
def ruta_descriere():
    return descriere()

@app.route('/Norvegia/capitala')
def ruta_capitala():
    return capitala()

@app.route('/Norvegia/steag')
def ruta_steag():
    return steag()

if __name__ == '__main__':
    app.run(debug=True)
