**Proiect SCC – Danemarca**
---
**Dezvoltator: Marcu Răzvan-Daniel**
---
**Descriere:**
---
În cadrul cursului Servicii de cloud şi containerizare, se va realiza proiectul pentru tema “Ţări” prin implementarea unor tehnologii, precum: Flask, Docker, Jenkins şi GitHub.

**Obiectivul proiectului:**
---
Realizarea unei aplicaţii web pentru Danemarca, care conţine trei endpoint-uri:”/danemarca”, “/danemarca/capitala”, “/danemarca/steag”). Folosind Flask, vor fi afişate informaţii corespunzătoarea fiecărui endpoint. De asemenea, proiectul cuprinde o parte dedicată testării automate prin intermediul Jenkins, iar secţiunea dedicată containerizării se va realiza prin Docker.

**Platforme şi tehnologii aplicate:**
---
**Flask**: Framework Python pentru dezvoltarea aplicaţiei web

**GitHub**: Permite gestionarea codului sursă şi a versiunilor în cadrul unei echipe

**Docker**: Permite rularea aplicaţiei în containere, asigurând un mediu izolat şi reproductibil

**Jenkins**: Folosit pentru automatizarea proceselor de testare şi livrare continuă a aplicaţiei

**Setare aplicaţie local:**
---
1.Configurare Git:

```bash
git config --global user.name "username"
```

```bash
git config --global user.email "email"
```

2.Clonare repository în directorul local:

```bash
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
```

```bash
cd curs_vcgj_4_tari
```

```bash
git checkout devel_marcu_razvan
```

3.Activare venv şi rularea aplicaţiei:

```bash
source activeaza_venv
```

```bash
source ruleaza_aplicatia
```

**Conţinutul proiectului (pentru a crea directoarele şi fişierele am folosit comenzile mkdir şi touch):**

![Continutul proiectului](/static/continut.png)
---
**Descrierea generală a fişierului tari.py:**
---
Fișierul tari.py are rolul de a configura aplicația web Flask și de a defini rutele prin care utilizatorii pot accesa informații despre Danemarca. Aplicația răspunde la cereri HTTP și afișează pagini HTML generate din șabloane, oferind conținut dinamic legat de descrierea țării, capitala acesteia și steagul național. Funcţiile implementate `descriere_danemarca()`, `capitala_danemarca()` şi `steag_danemarca()` au rolul de afişare a informaţiilor specifice fiecărei secţiuni.

Rutele definite în aplicație sunt accesibile prin metoda HTTP GET.

Aplicația oferă trei rute principale, fiecare fiind asociată unei pagini distincte:

1. Ruta pentru pagina principală (`/danemarca`)

Afișează o descriere generală a Danemarcei. Informațiile sunt preluate din funcțiile `index()` și `descriere_danemarca()`.

2. Ruta pentru capitala Danemarca (`/danemarca/capitala`)

Oferă detalii despre capitala țării, Copenhaga. Datele afișate sunt generate prin funcțiile `capitala()` și `capitala_danemarca()`.

3. Ruta pentru steagul Danemarcei (`/danemarca/steag`)

Prezintă informații legate de steagul național. Informațiile sunt furnizate de funcțiile `steag()` și `steag_danemarca()`.

**Containerizarea aplicației folosind Docker - executată din folder-ul cu Dockerfile-ul:**
---
1. Crearea imaginii Docker (include codul aplicaţiei, configuraţiile care asigură execuţia şi dependenţele Python):

```bash
sudo docker build -t tari:v01 .
```
![Imagine docker](/static/imagine_docker.png)

![Imagini docker](/static/imagini_docker.png)

2. Rulare container (containerul este accesibil prin maparea portului 5011 pe 8020 prin browser): 

```bash
sudo docker run --name tari -p 8020:5011 tari:v01
```
3. Acces browser:

```
http://127.0.0.1:8020/danemarca
```
![Rulare container](/static/browser_container.png)

**Prezentare Dockerfile:**
---
1. Selectarea imaginii de pornire  
Se utilizează `python:3.10-alpine`, o imagine compactă și eficientă pentru rularea aplicației.

2. Definirea aplicației Flask  
Este setată variabila de mediu `FLASK_APP=tari` pentru a indica fișierul principal al aplicației.

3. Rularea cu utilizator non-administrator  
Pentru o mai bună securitate, aplicația este rulată sub un utilizator non-root, numit `tari`.

4. Structurarea spațiului de lucru al aplicației  
Se creează un director dedicat aplicației, iar fișierele necesare sunt copiate în container.

5. Gestionarea pachetelor necesare  
Dependențele sunt instalate într-un mediu virtual Python, izolat de sistemul de bază.

6. Configurarea permisiunilor fișierelor  
Sunt aplicate permisiuni adecvate pentru script-uri, fișiere statice și directoare.

7. Publicarea portului aplicației  
Este expus portul 5011, permițând accesul din afara containerului.

8. Inițializarea serverului Flask  
Aplicația este pornită cu ajutorul scriptului `dockerstart.sh`, care execută comanda necesară pentru lansarea serverului Flask.

**Testarea cu pytest:**
---
Pentru verificarea funcţiilor şi a conţinutului prezentat de acestea în format HTML, vom implementa teste prin framework-ul Python `pytest`. În urma efectuării unui test, va fi afişat rezultatul `PASS` pentru testele validate, iar în cazul unui test eronat va fi prezentat rezultatul `FAIL`.

![Testare pytest](/static/pytest.png)
---

**Testare cu pylint:**
---

![Testare pylint](/static/testare_pylint.png)
---

**Jenkins:**
---
În cadrul Jenkins, testele sunt automatizate şi vor rula prin intermediul fişierului `Jenkinsfile`. Acesta va asigura ulterior configurarea pipeline-ului.

1. Verificare status Jenkins şi pornirea server-ului Jenkins:

```bash
systemctl status jenkins
```

```bash
jenkins
```

2. Accesare Jenkins:

```
localhost:8080
```

**Configurare proiect Jenkins pipeline:**
![Creare Jenkins](/static/crearejenkins.png)

![Configurare Jenkins](/static/configurarejenkins.png)

`Jenkinsfile` definește pipeline-ul de integrare continuă (CI) și livrare continuă (CD) pentru aplicația Flask, automatizând procesul de construire, testare și livrare.

**Etapele pipeline-ului:**

![Pipeline](/static/pipeline.png)

![BlueOcean](/static/blueocean.png)

- **Build** – Creează imaginea Docker a aplicației folosind `Dockerfile` și o etichetează cu numărul curent al build-ului.
- **Verificare calitate cod (pylint)** – Analizează codul sursă cu `pylint`.
- **Testare unitară (pytest)** – Rulează testele cu `pytest`.
- **Deploy** – Construiește imaginea finală pentru rulare în container.
- **Running** – Lansează aplicația pe portul 8020 pentru testare.

**GitHub şi Pull Request:**
---
Proiectul a fost dezvoltat în branch-ul `devel_marcu_razvan`, implementat local şi testat cu `pytest` şi `Jenkins`.

**Pull Request-uri proprii:**

```
PR #23 - Test PR 1
```

**Pull Request-uri efectuate:**

```
PR #22 - Actualizare aplicaţie 2
```
