## BULGARIA - Mirica Lidia - Cristiana

## CUPRINS
- [Pasii pentru realizarea proiectului](#pasii-pentru-realizarea-proiectului)
- [Descrierea fisierului tari.py](#descrierea-fisierului-tari.py)
- [Rularea aplicatiei cu Docker](#rularea-aplicatiei-cu-docker)
- [Testare](#testare)
Tema proiectului este dezvoltarea unei aplicatii simple pentru tara Bulgaria, utilizand Flask pentru a furniza informatii, Jenkins pentru testarea automata, GitHub pentru integrarea codului si Docker pentru containerizarea aplicatiei.

## Pasii pentru realizarea proiectului

1.	Adaugam numele si emailul utilizatorului folosint comenzile:
```bash
 git config --global user.name "username"
 git config --global user.email "email"
```
2.	In directorul in care am lucrat clonam repo-ul 
```bash
 git clone https://github.com//curs_vcgj_4_tari.git -> cd curs_vcgj_4_tari
```
3.	Crearea mediului virtual 
```bash
python3 -m venv .venv
```
4.	Activarea mediului virtual 
```bash
 source .venv/bin/activate
```
5.	Crearea directoarelor si fisierelor necesare utilizand comenzile mkdir si touch 
[!structura](/static/structura.png)
6.	Instalarea dependentelor 
```bash
pip install -r requirments.txt
```
7.	Pornirea aplicatiei Flask 
```bash
export FLASK_APP=tari -> flask run -p 5011 –reload
```
## Descrierea fisierului tari.py

Fișierul tari.py implementează o aplicație Flask care furnizează informații despre Bulgaria. Acesta include trei rute esențiale:
•	Descrierea Bulgariei
•	Capitala Bulgariei
•	Steagul Bulgariei
Fișierul tari.py are rolul de a configura aplicația web creată cu Flask, oferind informații despre Bulgaria prin intermediul a trei rute. Acesta gestionează logica de bază a aplicației și legătura cu fișierele HTML care vor fi afișate utilizatorului.

 **Importul modulelor necesare**
 
1.	Flask: biblioteca principală pentru dezvoltarea aplicației web.
2.	render_template: funcție ce permite încărcarea și afișarea de șabloane HTML.
3.	biblioteca_header și biblioteca_bulgaria: fișiere auxiliare care conțin funcții ce returnează  descrieri pentru paginile aplicației.

 **Inițializarea aplicației Flask** 
 
Se creează o instanță Flask folosind: api = Flask(__name__)
Parametrul __name__ este utilizat pentru ca Flask să poată localiza corect resursele aplicației (șabloane HTML, fișiere statice etc.).

 **Definirea rutelor principale:**
 
 Aplicația răspunde la trei adrese URL, fiecare furnizând informații diferite:
1.	 Ruta "Descriere Bulgaria" 
•	Când utilizatorul accesează pagina principală (/), aplicația returnează o pagină HTML cu o prezentare generală a Bulgariei.
•	Informațiile afișate provin din funcțiile header_descriere() și descriere_bulgaria() din modulele biblioteca_header si  biblioteca_bulgaria.
2.  Ruta "Capitala Bulgariei" (/capitala)
•	La această adresă, aplicația returnează capitala țării.
•	Conținutul este generat cu ajutorul funcțiilor header_capitala() și capitala_bulgaria().
3. Ruta "Steagul Bulgariei" (/steag)
•	Accesând această cale, utilizatorul primește o pagină ce afiseaza o imagine cu steagul Bulgariei.
•	Se folosesc funcțiile header_steag() și steag_bulgaria() pentru a completa pagina.

 **Pornirea aplicatiei Flask:** 
comanda api.run(debug=True, port=5011) pornește serverul Flask pe portul 5011, iar comanda debug=True activarea modului de depanare, care permite aplicației să se reîncarce automat atunci când se fac modificări și să afișeze erorile în consolă.
Aplicația este configurată pentru a rula pe portul 5011 și poate fi ușor extinsă pentru a adăuga funcționalități suplimentare.

## Rularea aplicatiei cu Docker

**Construirea imaginii Docker**

```bash
docker build -t 
```

**Rularea containerului** 

```bash
docker run -dp 5011:5011 
```
**Accesarea aplicatiei:** 

Deschidem browserul la http://localhost:8020 
În cadrul acestui proiect, Docker este folosit pentru a crea un mediu izolat în care rulează aplicația web construită cu Flask. Fișierul Dockerfile conține instrucțiunile necesare pentru a construi imaginea containerului pas cu pas:
1. Alegerea imaginii de bază
Se folosește o versiune minimalistă și rapidă de Python – python:3.10-alpine – ca bază pentru container. Această alegere asigură un sistem de operare compact, ideal pentru rularea aplicației în condiții eficiente.
2. Configurarea aplicației Flask
Este setată variabila de mediu FLASK_APP pentru ca Flask să știe care fișier trebuie executat ca punct de pornire al aplicației.
3. Utilizator non-root pentru rulare
Pentru a crește securitatea, aplicația este configurată să ruleze cu un utilizator dedicat (numit tari), evitând privilegiile de root în interiorul containerului.
4. Organizarea mediului de lucru
Se creează un director special în container pentru aplicație, unde sunt copiate toate fișierele proiectului. Acest lucru ajută la menținerea structurii organizate.
5. Instalarea pachetelor necesare
Pentru a rula aplicația, sunt instalate toate dependențele specificate, folosind un mediu virtual de Python. Acest pas asigură că toate librăriile sunt izolate și compatibile.
6. Permisiuni și acces
Fișierele aplicației (inclusiv cele statice și scripturile) primesc permisiuni adecvate, astfel încât să poată fi accesate corect de către utilizatorul tari.
7. Expunerea portului aplicației
Portul 5011 este deschis pentru a permite accesul la aplicația web din afara containerului.
8. Pornirea aplicației
La final, aplicația Flask este lansată cu ajutorul unui script numit dockerstart.sh, care conține comanda necesară pentru a rula aplicația în container.

## Testare

•	Testare cu pytest folosind comanda 
```bash
    pytest app/tests/
```
•	Fișierul pytest.ini este un fișier de configurare folosit de framework-ul de testare pytest pentru a controla comportamentul testelor. 
•	Validare cod cu pylint : 
```bash
pylint tari.py
```
•	Testare cu Jenkins avand urmatoarele etape 
    •  Build: Creează imaginea Docker și o etichetează cu numărul build-ului.
    •  pylint: Verifică stilul și calitatea codului.
    •  Testare: Rulează testele unitare cu pytest.
    •  Deploy: Construiește și rulează imaginea Docker pe portul 8020.
    •  Post: Curăță mediul, oprind și ștergând containerele rămase active.
[!jenkins](/static/jenkins.png)






