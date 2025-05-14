Proiect SCC - Olanda

Descriere

Acest proiect este dedicat temei "Tari", in cadrul cursului Servicii Cloud si Cointainerizare, folosind tehnologii precum Flask, Docker, Jenkins si Git/GitHub

Obiectivul proiectului

Proiectul urmareste dezvoltarea unei aplicatii simple pentru Olanda, utilizand Flask
pentru a furniza informatii despre tara: o mica descriere, capitala acesteia si steagul,
prin 3 endpoint-uri "/", "/capitala" si "/steag".
Proiectul include si testarea automata folosind Jenkins, integrarea codului prin GitHub, si containerizarea aplicatiei folosind Docker.

Tehnologii folosite

Flask: Framework Python pentru dezvoltarea aplicatiei web.
Docker: Containere pentru rularea aplicatiei intr-un mediu izolat.
Jenkins: Automatizarea testarii si livrarii aplicatiei.
Git/GitHub: Colaborare si versionare a codului sursa.

Rularea aplicatiei local

Setam numele si emailul utilizatorului care va fi asociat cu toate commit-urile facute pe masina
-> git config --global user.name "username"
-> git config --global user,email "email"

Clonam repo-ul in direcotorul de lucru

git clone https://github.com/<user>/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari

Crearea si activarea mediului virtual

-> python3 -m venv .venv
-> source .venv/bin/activate

Crearea directoarelor si fisierelor necesare proiectului cu comenzile mkdir si touch
Structura proiect:
![Structura](/home/daniela/proiect/curs_vcgj_4_tari/static/)

Instalarea dependentelor

-> pip install -r requirments.txt

Pornirea aplicatiei Flask

-> export FLASK_APP=tari
-> flask run -p 5011 --reload

Rularea aplicatiei cu Docker (in folderul in care se afla Dockerfile)

Construirea imaginii Docker 
-> docker build -t <nume>
Rularea containerului
-> docker run -dp 5011:5011 <nume>
Accesarea aplicatiei
-> Deschidem browserul la http://localhost:8020

Testare

Testare unitara cu pytest
-> pytest app/tests/
Testare cu Jenkins
Testele sunt automatizate si vor rula pe Jenkins, folosind fisierul Jenkinsfile pentru a configura pipeline-ul.

