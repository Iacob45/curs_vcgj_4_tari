## EGIPT - Mirescu Monica-Elena

## Cuprins

- Implementare functionalitate
- Rularea locala a aplicatiei
- Rularea aplicatiei cu Docker
- Testare cu pytest
- Testare automata cu Jenkins
  


## Implementare functionalitate

Aplicația egipt_app din cadrul proiectului SCC 2025 își propune să demonstreze un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă. 

 
 Biblioteca de funcții

În app/lib/biblioteca_egipt.py am definit trei funcții:
	
 	descriere_egipt(), care oferă informații generale despre tara
  
  	capitala_egipt(), care returneaza capitala tarii
   
   	steag_egipt(), care returneaza drapelul tarii

	    
 Server Flask

În tari.py am creat un server Flask cu trei rute:

        /egipt – pagina principală, cu linkuri către subpagini

        /capitala – afișează capitala Egiptului

        /steag – afișează drapelul Egiptului



## Rularea locala a aplicatiei

Ruleaza intr-un terminal de linux urmatoarele 2 comenzi:

git clone --branch main_mirescu_monica https://github.com/Iacob45/curs_vcgj_4_tari.git

cd curs_vcgj_4_tari

Deschide in browser: http://127.0.0.1:5011/egipt
     		

Rulez testele local cu:

    export PYTHONPATH = $(pwd) 
    pytest



## Rularea aplicatiei cu Docker

  Containerizare Docker

Fișierul Dockerfile definește o imagine pe bază de python:3.12-slim, copiază codul, instalează dependențele din requirements.txt și pornește serverul Flask.

Local, imaginea e construită cu:

	docker build -t egipt_app .

Și rulează astfel:

	docker run -p 5011:5000 egipt_app



## Testare cu pytest
	
 Testele sunt definite in tests/test_biblioteca_egipt.py si verifica urmatoarele:

  	descriere_egipt() returnează un șir de minim 10 caractere

	capitala_egipt() returnează capitala tarii, si anume "Cairo"

Rulez testele local cu:

    export PYTHONPATH = $(pwd) 
    pytest



## Testare automata cu Jenkins

Am definit un Jenkinsfile în modul declarativ, cu etape de:

	Checkout – preia codul din branch-ul main_mirescu_monica

        Install – pip install -r requirements.txt

        Test – pytest --maxfail=1 --disable-warnings -q

	Build Docker Image – docker build -t egipt_app .

	Run Docker Image - docker run -d --name egipt_container -p 5011:5000 egipt_app

Jenkins rulează pipeline-ul la fiecare push, asigurându-se că codul e testat și containerul poate fi construit.



În ansamblu, proiectul demonstrează întregul ciclu de viață al unei aplicații: de la scrierea codului și testare, la containerizare și automatizare CI/CD, toate acestea fiind bine documentate în README pentru ușurința utilizării și prezentării.

