# Tutorial
1. Asigură-te că Make este instalat pe sistem (ex. sudo apt install make pe Ubuntu).

2. Ruleaza intr-un terminal de linux urmatoarele 3 comenzi:

git clone --branch main_ion_filip https://github.com/nikq51/curs_SCC_25_animale.git

cd curs_SCC_25_animale

make all

3.  Deschide in browser 
http://localhost:5000/alpaca
-------------sau-----------------
http://127.0.0.1:5000/alpaca

# Despre proiect

Aplicația Alpaca App din cadrul proiectului SCC 2025 (student Ion Filip-Viorel, grupa 441D) își propune să demonstreze un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă. Principalii pași parcurși sunt:

   Biblioteca de funcții pentru Alpaca

        În app/lib/biblioteca_animale.py am definit două funcții:

            culoare_alpaca(), care returnează o descriere a culorii lânii alpaca

            descriere_alpaca(), care oferă informații generale despre animal
	    
Server Flask

        În app/main.py am creat un server Flask cu trei rute:

            /alpaca – pagina principală, cu linkuri către subpagini

            /culoare_alpaca – afișează rezultatul lui culoare_alpaca()

            /descriere_alpaca – afișează rezultatul lui descriere_alpaca()

        Am folosit render_template_string pentru a genera rapid un meniu simplu cu hyperlink-uri.

   Teste automatizate cu pytest

        În tests/test_biblioteca_animale.py am scris teste care:

            verifică că culoare_alpaca() returnează un șir de caractere ce conține o culoare

            verifică că descriere_alpaca() returnează un șir de minim 10 caractere

   Rulez testele local cu:

    PYTHONPATH=$(pwd) pytest

Containerizare Docker

    Fișierul Dockerfile definește o imagine pe bază de python:3.12-slim, copiază codul, instalează dependențele din requirements.txt și pornește serverul Flask.

    Local, imaginea e construită cu:

	docker build -t alpaca_app .

	Și rulează astfel:

    docker run -p 5000:5000 alpaca_app

Automatizare CI/CD cu Jenkins

    Am definit un Jenkinsfile în modul declarativ, cu etape de:

        Checkout – preia codul din branch-ul main_ion_filip

        Install – pip install -r requirements.txt

        Test – pytest --maxfail=1 --disable-warnings -q

        Build Docker Image (opțional) – docker build -t alpaca_app .

    Jenkins rulează pipeline-ul la fiecare push, asigurându-se că codul e testat și containerul poate fi construit.

Makefile

	Un makefile este practic un script ce poate fi rulat cu "make" pentru a compila un executabil binar final.

    În rădăcina repo-ului am adăugat un Makefile cu ținte:

        make build – construiește imaginea Docker

        make run – pornește containerul (după ce oprește oricare instanță anterioară)

        make stop – oprește și șterge containerul

        make all – rulează build și run într-o singură comandă

    Astfel, utilizatorii pot porni tot fluxul local cu:

        make all

În ansamblu, proiectul demonstrează întregul ciclu de viață al unei aplicații: de la scrierea codului și testare, la containerizare și automatizare CI/CD, toate acestea fiind bine documentate în README pentru ușurința utilizării și prezentării.

