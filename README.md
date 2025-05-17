**Proiect SCC – Danemarca**

**Descriere:**

În cadrul cursului Servicii de cloud şi containerizare, se va realiza proiectul pentru tema “Ţări” prin implementarea unor tehnologii, precum: Flask, Docker, Jenkins şi GitHub.

**Obiectivul proiectului:**

Realizarea unei aplicaţii web pentru Danemarca, care conţine trei endpoint-uri:”/danemarca”, “/danemarca/capitala”, “/danemarca/steag”). Folosind Flask, vor fi afişate informaţii corespunzătoarea fiecărui endpoint. De asemenea, proiectul cuprinde o parte dedicată testării automate prin intermediul Jenkins, iar secţiunea dedicată containerizării se va realiza prin Docker. 

**Platforme şi tehnologii aplicate:**

->Flask: Framework Python pentru dezvoltarea aplicaţiei web

->GitHub: Permite gestionarea codului sursă şi a versiunilor în cadrul unei echipe 

->Docker: Permite rularea aplicaţiei în containere, asigurând un mediu izolat şi reproductibil

->Jenkins: Folosit pentru automatizarea proceselor de testare şi livrare continuă a aplicaţiei

**Setare aplicaţie local:**

- Configurare Git:

`            `git config --global user.name "username"

`            `git config --global user.email "email"

- Clonare repository în directorul local:

`            `git clone https://github.com/<user>/curs_vcgj_4_tari.git

`            `cd curs_vcgj_4_tari

- Setare mediul virtual de lucru:

`            `python3 -m venv .venv

`            `source .venv/bin/activate

**Conţinutul proiectului** (pentru a crea directoarele şi fişierele am folosit comenzile mkdir şi touch):

- Instalarea dependenţelor:

`            `pip install -r requirements.txt

- Lansare aplicaţie Flask:\
  export FLASK_APP=tari

  flask run -p 5011 –reload

**Descrierea generală a fişierului tari.py:**
**\
\
Fișierul tari.py are rolul de a configura aplicația web Flask și de a defini rutele prin care utilizatorii pot accesa informații despre Danemarca. Aplicația răspunde la cereri HTTP și afișează pagini HTML generate din șabloane, oferind conținut dinamic legat de descrierea țării, capitala acesteia șisteagul național.

Rutele definite în aplicație

Aplicația oferă trei rute principale, fiecare corespunzând unei pagini distincte:

1\. Ruta pentru pagina principală ("/danemarca")

- Afișează o descriere generală a Danemarca.
- Informațiile sunt preluate din funcțiile index() și descriere\_danemarca().

2\. Ruta pentru capitala Danemarca ("/damemarca/capitala")

- Oferă detalii despre capitala țării, Copenhaga.
- Datele afișate sunt generate prin funcțiile capitala() și capitala\_danemarca().

3\. Ruta pentru steagul Danemarcei ("/danemarca/steag")

- Prezintă informații legate de steagul național.
- Informațiile sunt furnizate de funcțiile steag() și steag\_danemarca().

Containerizarea aplicației folosind Docker, executată din folderul cu Dockerfile-ul:

Creare imagine Docker:

sudo docker build -t tari:v01 .

Rulare container: 

sudo docker run --name tari -p 8020:5011 tari:v01

Acces browser:

<http://127.0.0.1:8020/danemarca>

**Prezentare Dockerfile:**

- Selectarea imaginii de pornire

`            `Se utilizează python:3.10-alpine, o imagine compactă și eficientă pentru rularea aplicației.

- Definirea aplicației Flask

`            `Este setată variabila de mediu FLASK\_APP tari pentru a indica fișierul principal al aplicației.

- Rularea cu utilizator non-administrator

`            `Pentru o mai bună securitate, aplicația este rulată sub un utilizator non-root, numit ţări.

- Structurarea spațiului de lucru al aplicației

`            `Se creează un director dedicat aplicației, iar fișierele necesare sunt copiate în container.

- Gestionarea pachetelor necesare

`            `Dependențele sunt instalate într-un mediu virtual Python, izolat de sistemul de bază.

- Configurarea permisiunilor fișierelor

`            `Sunt aplicate permisiuni adecvate pentru script-uri, fișiere statice și directoare.

- Publicarea portului aplicației

`            `Este expus portul 5011, permițând accesul din afara containerului.

- Inițializarea serverului Flask

`            `Aplicația este pornită cu ajutorul script-ului dockerstart.sh, care execută comanda necesară pentru lansarea serverului Flask.

**Testarea cu pytest:**

**Jenkins:**

În cadrul Jenkins, testele sunt automatizate şi vor rula prin intermediul fişierului Jenkinsfile. Acesta va asigura ulterior configurarea pipeline-ului.

- Pornire server Jenkins:

  jenkins

- Accesare Jenkins:

  localhost:8080

Configurare proiect Jenkins pipeline:

Descriere Jenkinsfile: Jenkinsfile definește pipeline-ul de integrare continuă (CI) și livrare continuă (CD) pentru aplicația Flask, automatizând procesul de construire, testare și livrare.

**Etapele pipeline-ului:**

- Build

  Creează imaginea Docker a aplicației folosind Dockerfile-ul din proiect și o etichetează cu numărul curent al build-ului.

- Verificare calitate cod (pylint)

  Analizează codul sursă cu pylint pentru a identifica erori de stil și probleme potențiale, contribuind la menținerea unui cod curat și conform standardelor.

- Testare unitară (pytest)

  Rulează testele unitare cu pytest pentru a valida funcționalitatea aplicației și a preveni regresiile.

- Deploy

  ` `Construiește imaginea finală a aplicației, pregătită pentru rulare într-un container Docker.

- Running

  Lansează containerul Docker și expune aplicația local pe portul 8020, făcând-o accesibilă pentru testare sau utilizare.

- Post

  Asigură curățarea mediului prin oprirea și eliminarea automată a containerelor rămase active după rularea pipeline-ului.




