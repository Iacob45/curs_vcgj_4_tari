## MALTA - Nanu Ana-Maria

##  CUPRINS

- [Descriere](#descriere) 
- [Obiectiv](#obiectiv) 
- [Stadiu curent](#stadiu-curent)
- [Tehnologii folosite](#tehnologii-folosite) 
- [Crearea și activarea mediului virtual](#crearea-și-activarea-mediului-virtual) 
- [Structura și fișierele proiectului](#structura-și-fișierele-proiectului) 
- [Instalarea dependințelor](#instalarea-dependențelor) 
- [Implementare functionalitati](#implementare-functionalitati)
  - [`biblioteca_malta.py`](#descrierea-bibliotecii-malta)
  - [`tari.py`](#descrierea-fisierului-tari.py) 
- [Rularea locala a aplicatiei Flask](#rularea-locala-aplicatiei-flask)
- [Gestionarea codului cu Git & GitHub](#utilizarea-git--github)
  - [Flux de lucru cu Git si Pull Request-uri](#flux-de-lucru-cu-git-si-pull-request-uri)
  - [Integrare si colaborare GitHub](#integrare-si-colaborare-github) 
- [Containerizare cu Docker](#containerizare-cu-docker) 
  - [Descriere Dockerfile](#descriere-dockerfile) 
- [Testare](#testare)
  - [Testare unitara cu pytest](#testare-unitara-cu-pytest) 
  - [Testare automata (Jenkins)](#testare-automata-cu-jenkins) 
  - [Descriere Jenkinsfile](#descriere-jenkinsfile) 

## Descriere

Proiectul prezintă o aplicație web informativă despre Republica Malta, realizată în cadrul cursului Servicii Cloud și Containerizare, folosind tehnologii precum Flask, Docker, Jenkins și Git/GitHub.

## Obiectiv

Acest proiect își propune dezvoltarea unei aplicații web minimaliste, construită cu **Flask**, care oferă utilizatorilor informații esențiale despre Republica Malta — o descriere succintă a țării, detalii despre capitală și prezentarea drapelului — prin intermediul a trei endpoint-uri: `/malta`, `/malta/capitala` și `/malta/steag`. În plus, fluxul de lucru include teste automate orchestrate de **Jenkins**, controlul versiunilor și revizuirea codului prin **Git/GitHub**, precum și containerizarea întregii aplicații cu **Docker**.

## Stadiu curent
**Stadiul implementarii:** funcționalitate completă, testare finalizată, integrare realizată în branch-ul principal `main_nanu_ana`.

## Tehnologii folosite

- Flask: Framework Python pentru dezvoltarea aplicatiei web.
- Docker: Containere pentru rularea aplicatiei intr-un mediu izolat.
- Jenkins: Automatizarea testarii si livrarii aplicatiei.
- Git/GitHub: Colaborare si versionare a codului sursa.


## Crearea si activarea mediului virtual

```bash
 python3 -m venv .venv
 source .venv/bin/activate
```
## Structura și fișierele proiectului

![Structura](/static/structura.png)

## Instalarea dependintelor
```bash
pip install -r requirements.txt
```
![Structura](/static/requirements.png)


## Implementare functionalitati 

### `biblioteca_malta.py`

Fișierul **`biblioteca_malta.py`** are rolul de a centraliza toată logica de generare a interfeței HTML (conținut + CSS) pentru paginile dedicate Maltei. În esență:

1. **`base_css()`**
   - Definește în interiorul unui bloc `<style>` stilurile comune ale tuturor paginilor:
     - Importă fontul Montserrat de la Google Fonts  
     - Declară variabile CSS (culori primare, gradient de fundal, fundal de card semi‐translucent, accente de hover etc.)  
     - Setează reguli globale de box‐sizing, margin/padding zero, font‐family și line‐height  
     - Stilizează structura de tip card și efectele de hover  
     - Configurează clasa `.hero` pentru banner‐uri parallax cu gradient de suprapunere  
     - Pregătește layout‐ul containerelor, butoanelor și imaginilor inline  

2. **`descriere_malta()`**
   - Apelează `base_css()` pentru a injecta CSS‐ul în pagină  
   - Construiește o pagină HTML cu:
     - Un banner hero care folosește `/static/malta_bg.jpg`  
     - Titlul “Malta 🇲🇹”  
     - Trei paragrafe cu informații despre istoria, clima și economia Maltei  
     - Un set de butoane de navigare către paginile de capitală și steag  

3. **`capitala_malta()`**
   - Reia `base_css()` pentru stilizare  
   - Creează un banner hero cu imaginea Vallettei (`/static/valletta.jpg`)  
   - Afișează un titlu și trei paragrafe despre fondarea și arhitectura capitalei  
   - Inserează o imagine inline (`/static/valletta_strazi.jpg`) care ilustrează străzile iconice  
   - Include butoane “Înapoi la Descriere” și “Vezi Steagul” pentru navigare  

4. **`steag_malta()`**
   - Reaplică `base_css()` pentru consistență vizuală  
   - Generează un banner hero cu `/static/steag_malta_banner.jpg`  
   - Oferă două paragrafe despre semnificația culorilor și a Crucii Sfântului Gheorghe  
   - Inserează imaginea propriu‐zisă a steagului (`/static/steag_malta.png`)  
   - Pune la dispoziție butoanele de navigare “Descriere” și “Vezi Capitala”  

---

**Pe scurt**, acest modul convertește datele și imaginile statice într‐un șablon HTML+CSS coerent și modern, pregătit pentru a fi returnat direct de către rutele Flask (`/malta`, `/malta/capitala`, `/malta/steag`). Separarea clară a funcțiilor de stil (`base_css`) de cele de conținut (`descriere_malta`, `capitala_malta`, `steag_malta`) face codul ușor de întreținut și de extins.

---
### `tari.py`

Fișierul **`tari.py`** definește aplicația Flask și asigură mapping-ul între URL-uri și paginile HTML generate pentru Malta:

```python
from flask import Flask, url_for
from app.lib import biblioteca_malta

api = Flask(__name__)
````

* **`from flask import Flask, url_for`**
  Importă clasa `Flask` necesară pentru inițializarea aplicației și `url_for` pentru generarea dinamică a link-urilor interne.
* **`from app.lib import biblioteca_malta`**
  Încarcă modulul care conține funcțiile de generare HTML (`descriere_malta()`, `capitala_malta()`, `steag_malta()`).

```python
api = Flask(__name__)
```

* Creează o instanță a aplicației Flask numită `api`.
* Argumentul `__name__` permite Flask să găsească corect resursele statice și template-urile.

```python
@api.route("/malta", methods=['GET'])
def index() -> str:
    return biblioteca_malta.descriere_malta()
```

* **Ruta `/malta`**

  * Metoda HTTP: `GET`
  * Handler: funcția `index()` returnează rezultatul `descriere_malta()`, pagina de descriere generală a Maltei.

![Descriere](/static/descriere.png)

```python
@api.route("/malta/capitala", methods=['GET'])
def capitala() -> str:
    return biblioteca_malta.capitala_malta()

```

* **Ruta `/malta/capitala`**

  * Metoda HTTP: `GET`
  * Handler: `capitala()` returnează HTML-ul cu informații detaliate despre capitală.

![Capitala](/static/capitala.png)

```python
@api.route("/malta/steag", methods=['GET'])
def steag() -> str:
    return biblioteca_malta.steag_malta()
```

* **Ruta `/malta/steag`**

  * Metoda HTTP: `GET`
  * Handler: `steag()` returnează pagina cu drapelul Maltei.

![Steag](/static/steag.png)

---

**Rolul fișierului**:

* Centralizează configurația aplicației și alocarea celor trei endpoint-uri principale.
* Păstrează separarea responsabilităților:

  * **`tari.py`** se ocupă doar cu definirea rutelor și inițializarea Flask.
  * **`biblioteca_malta.py`** conține logica de generare a conținutului și stilurilor HTML.

Această structură modulară asigură claritate, testabilitate și ușurință în extinderea aplicației (adăugare de noi pagini sau funcționalități).


## Rularea locala a aplicatiei Flask
```bash
flask --app tari run
```

## Gestionarea codului cu Git & GitHub

Setam numele si emailul utilizatorului care va fi asociat cu toate commit-urile facute pe masina

```bash
 git config --global user.name "username"
 git config --global user.email "email"
```
Clonam repo-ul in direcotorul de lucru
```bash
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
```
Crearea branchurilor individuale

```bash
git branch devel_nanu_ana
git branch main_nanu_ana
```
Mutarea pe branch-ul devel
```bash
git branch devel_nanu_ana
```
Adaugarea fisierelor modificate
```bash
git add .
git commit -m "Mesajul de commit"
```
Aducem modificarile pe GitHub
```bash
git push origin devel_nanu_ana
```
### Flux de lucru Git și Pull Request-uri

Pentru dezvoltarea suportului pentru Malta am urmat un workflow bazat pe branch-uri, după cum urmează:

1. Am creat un branch de feature **`devel_malta_ana`**, unde am implementat toate funcțiile și stilurile necesare (CSS, `descriere_malta()`, `capitala_malta()`, `steag_malta()`).
2. Pe măsură ce finalizam fiecare sub‐task (CSS, conținut, teste), am făcut commit-uri cu mesaje descriptive:  
   - `feat: add base_css and descriere_malta`  
   - `feat: implement capitala_malta page`  
   - `test: add pytest for biblioteca_malta`  
3. După ce tot codul a trecut testele locale (`pytest`, `pylint`) și rularea manuală, am deschis un **Pull Request** din `devel_malta_ana` către `main_malta_ana`:
   - **PR #12** – Adăugare suport Malta: descriere, capitală, steag  
4. În PR am inclus rezultatele rulărilor automate din Jenkins (capturi ecran + status PASS) și instrucțiuni de testare manuală.

Fiecare PR a trecut printr-un proces de code review, pentru a ne asigura că stilul și calitatea codului sunt conforme cu standardele proiectului.

---

### Integrare și colaborare GitHub

Pentru fiecare Pull Request am respectat următoarele bune practici GitHub:

- **Descriere completă** a schimbărilor și modul de testare.  
- **Link-uri** către build-urile relevante din Jenkins.  
- Etichete (labels) „feature”, „CI passed” și „ready for review”.  
- Eliminarea oricăror conflicte de merge înainte de aprobare.


## Containerizare cu Docker

În directorul proiectului (unde se află `Dockerfile`):

```bash
# Build și etichetare imagine
docker build -t tari_malta:v01 .

# Pornire container (mapare port host 8020 → container 5011)
docker run --rm -d --name malta_app -p 8020:5011 tari_malta:v01
```

Accesează aplicația la `http://localhost:8020/malta`

---

### Descriere Dockerfile

* **FROM:** `python:3.10-alpine`
* **ENV FLASK\_APP=tari**
* **USER non-root:** `adduser -D tari` + `USER tari`
* **WORKDIR:** `/home/ana/proiect_scc/curs_vcgj_4_tari/`
* **COPY:** cod, static, scripturi, `requirements.txt`
* **RUN:**

  * `python3 -m venv .venv`
  * `.venv/bin/pip install -r requirements.txt`
  * `chmod +x dockerstart.sh`
* **EXPOSE:** `5011`
* **ENTRYPOINT:** `./dockerstart.sh`
* **CMD:** `flask run --host=0.0.0.0 --port=5011`


## Testare

### Testare unitară cu pytest

Rulează toate testele din `app/tests/` cu:

```bash
pytest -q
```

* Testele sunt configurate în `pytest.ini`:

  * `pythonpath = .` (importă modulele din proiect)
  * `testpaths = app/tests` (rulează doar testele din acest folder)

---

### Testare automată (Jenkins)

* Pipeline-ul este definit în `Jenkinsfile` și pornește la fiecare push sau Pull Request.
* Etapele principale:

  1. **Setup** – creare și activare `.venv`, instalare dependențe
  2. **Lint** – `pylint` pe cod și teste
  3. **Unit Tests** – `pytest`
  4. **Docker Build & Run** – construiește și pornește containerul

Astfel, fiecare schimbare este verificată automat pentru calitate și funcționalitate.
![Configurare pipeline](/static/configurare-pipeline.png)
![Overview](/static/pipeline-overview.png)
![BlueOcean](/static/blueocean.png)

### Descriere Jenkinsfile

Fișierul **`Jenkinsfile`** definește un pipeline declarativ de CI/CD pentru aplicația Malta, cu obiectivul de a asigura consistență, calitate și rulare automată. Iată rolul și motivația fiecărei secțiuni:

- **`agent any`**  
  Permite executarea pe orice nod Jenkins disponibil, pentru flexibilitate și scalabilitate.

- **stage('Build')**  
  - *Scop:* Pregătirea mediului și construire imagine Docker inițială.  
  - *Pași:*  
    1. Se rulează scriptul `activeaza_venv_jenkins` pentru a crea/activa `.venv` și instala dependențe.  
    2. `docker build -t tari:v${BUILD_NUMBER} .` — etichetează imaginea cu numărul build-ului, garantând un identificator unic.

- **stage('pylint - calitate cod')**  
  - *Scop:* Verificarea stilului și a standardelor de cod înainte de testare.  
  - *Motivație:* Detectarea timpurie a problemelor de calitate fără a opri pipeline-ul (`--exit-zero`).  
  - *Pași:*  
    1. Activare venv (`activeaza_venv`) și export `PYTHONPATH=.`, pentru ca pylint să importe modulele corect.  
    2. Rulare `pylint` pe fișierele din `app/lib/`, `app/tests/` și `tari.py`.

- **stage('Unit Testing cu pytest')**  
  - *Scop:* Validarea funcționalității prin teste automate.  
  - *Pași:*  
    1. Activare venv  
    2. `pytest app/tests/` — rulează toate testele unitare din proiect.

- **stage('Deploy')**  
  - *Scop:* Creare imagine Docker finală după validări.  
  - *Motivație:* Separă etapa de build inițial (pentru verificări rapide) de cea de producție.  
  - *Pași:*  
    - `docker build -t tari:v${BUILD_NUMBER} .`

- **stage('Running')**  
  - *Scop:* Rulare container pentru testare manuală sau demonstrație.  
  - *Pași:*  
    - `docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}`

- **post { always }**  
  - *Scop:* Curățare automată după fiecare build, împiedicând acumularea containerelor inactive.  
  - *Pași:*  
    ```bash
    docker stop tari${BUILD_NUMBER} || true
    docker rm   tari${BUILD_NUMBER} || true
    ```

---

**Rol:**  
1. **Claritate și separare:** Fiecare etapă are responsabilități precise (build, lint, test, deploy, run).  
2. **Reproducibilitate:** Venv-ul și imaginile Docker garantate de scripturi scrise în `activeaza_venv_jenkins` și `Dockerfile`.  
3. **Feedback rapid:** Lint și teste rulate automat ajută la identificarea și rezolvarea rapidă a erorilor.  
4. **Curățenie în mediu:** Secțiunea `post` asigură eliminarea containerelor, menținând nodul Jenkins curat.


