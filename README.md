# Proiect SCC - Portugalia

## Descriere

Acest proiect este dedicat temei "Tari", in cadrul cursului Servicii Cloud si Cointainerizare, folosind tehnologii precum Flask, Docker, Jenkins si Git/GitHub

## Obiectivul proiectului

Proiectul urmareste dezvoltarea unei aplicatii simple pentru Portugalia, utilizand Flask
pentru a furniza informatii despre tara: o mica descriere, capitala acesteia si steagul,
prin 3 endpoint-uri "/", "/capitala" si "/steag".
Proiectul include si testarea automata folosind Jenkins, integrarea codului prin GitHub, si containerizarea aplicatiei folosind Docker.

## Tehnologii folosite

- Flask: Framework Python pentru dezvoltarea aplicatiei web.
- Docker: Containere pentru rularea aplicatiei intr-un mediu izolat.
- Jenkins: Automatizarea testarii si livrarii aplicatiei.
- Git/GitHub: Colaborare si versionare a codului sursa.

## Rularea aplicatiei local

Crearea si activarea mediului virtual

```bash
 python3 -m venv .venv
 source .venv/bin/activate
```
Gestionarea codului cu Git si GitHub

Setam numele si emailul utilizatorului care va fi asociat cu toate commit-urile facute pe masina

```bash
 git config --global user.name "username"
 git config --global user,email "email"
```
Clonam repo-ul in direcotorul de lucru
```bash
git clone https://github.com/<user>/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
```
Crearea branchurilor individuale

```bash
git branch <devel_nume>
git branch <main_nume>
```
Ne mutam pe branch-ul devel
```bash
git branch <devel_nume>
```
Adaugarea fisierelor modificate
```bash
git add .
git commit -m "Mesajul de commit"
```
Aducem modificarile pe GitHub
```bash
git push origin <devel_nume>
```
Crearea unui Pull Request pentru a fuziona in branch ul principal <main_nume> modificarile aduse pe GitHub pe branch ul <devel_nume>

![Structura](/static/pullRequest.png)

Un Pull Request (PR) este o cerere de a integra modificările dintr-un branch într-un alt branch din același repository sau dintr-un repository diferit. Acesta este un proces folosit de obicei în Git și platformele de gestionare a codului sursă, precum GitHub, pentru a revizui și aproba modificările înainte ca acestea să fie adăugate în branch-ul principal al proiectului.

Un Pull Request include de obicei următoarele etape:

1. **Crearea unui branch**: Dezvoltatorul creează un branch dedicat pentru a adăuga noi funcționalități sau pentru a remedia erori.

2. **Realizarea modificărilor**: Dezvoltatorul face modificările necesare în branch-ul său.

3. **Deschiderea unui Pull Request**: După ce modificările sunt finalizate, dezvoltatorul trimite un PR pentru a solicita integrarea acestor modificări în branch-ul principal (de obicei main sau master).

4. **Revizuirea PR-ului**: Alți membri ai echipei sau colaboratori ai proiectului pot verifica modificările, lăsa comentarii și solicita modificări suplimentare.

5. **Fuzionarea (merge)**: După ce PR-ul a fost revizuit și aprobat, modificările sunt integrate în branch-ul principal.

## Crearea directoarelor si fisierelor necesare proiectului cu comenzile mkdir si touch
Structura proiect:

![Structura](/static/structura.png)


Instalarea dependentelor
```bash
pip install -r requirments.txt
```
Pornirea aplicatiei Flask
```bash
export FLASK_APP=tari
flask run -p 5011 --reload
```
## Descriere `tari.py`

Fișierul **`tari.py`** este responsabil pentru configurarea aplicației web Flask și definirea rutelor care oferă informații despre Olanda. În acest fișier, se utilizează Flask pentru a crea o aplicație care răspunde la cereri HTTP și afișează pagini HTML cu informații despre Olanda.

1. **Importarea bibliotecilor necesare**
- **Flask**: Biblioteca principală folosită pentru a construi aplicația web.
- **render_template**: Permite încărcarea fișierelor HTML și le procesează pentru a le face disponibile utilizatorului.
- **biblioteca_header** și **biblioteca_olanda** sunt module interne care conțin funcții pentru a oferi titluri și descrieri pentru paginile din aplicație.

2. **Crearea aplicației Flask**
Fișierul inițializează aplicația Flask folosind comanda:

- **Flask(__name__)**: Creează o instanță a aplicației Flask, unde `__name__` ajută Flask să identifice locația aplicației pentru a căuta fișierele necesare (de exemplu, fișiere HTML).

3. **Definirea rutelor aplicației**

Aplicația definește trei rute principale, fiecare redirecționând către o pagină specifică:

3.1 **Ruta pentru pagina principală (Descrierea Olandei)**
- Această rută răspunde la cererile HTTP pe calea principală ("/").
- Pagina redirecționează utilizatorul către un fișier HTML care afișează o descriere a Olandei.
- Datele pentru titlu și descriere sunt obținute din funcțiile `header_descriere()` și `descriere_olanda()` din modulele `biblioteca_header` și `biblioteca_olanda`.

3.2 **Ruta pentru pagina cu capitala Olandei**
- Ruta aceasta răspunde la cererile HTTP pe calea "/capitala".
- Pagina redirecționează utilizatorul către un fișier HTML care afișează informații despre capitala Olandei.
- Datele pentru titlu și descrierea capitalei sunt obținute din funcțiile `header_capitala()` și `capitala_olanda()` din modulele `biblioteca_header` și `biblioteca_olanda`.

3.3 **Ruta pentru pagina cu steagul Olandei**
- Ruta aceasta răspunde la cererile HTTP pe calea "/steag".
- Pagina redirecționează utilizatorul către un fișier HTML care afișează informații despre steagul Olandei.
- Datele pentru titlu și descrierea steagului sunt obținute din funcțiile `header_steag()` și `steag_olanda()` din modulele `biblioteca_header` și `biblioteca_olanda`.

4. **Pornirea aplicației Flask**
- **api.run(debug=True, port=5011)**: Pornește serverul Flask pe portul 5011.
  - **debug=True**: Activarea modului de depanare, care permite aplicației să se reîncarce automat atunci când se fac modificări și să afișeze erorile în consolă.

Concluzie

Fișierul **`tari.py`** implementează o aplicație Flask care furnizează informații despre Olanda. Acesta include trei rute esențiale:
- Descrierea Olandei
- Capitala Olandei
- Steagul Olandei

Aplicația este configurată pentru a rula pe portul 5011 și poate fi ușor extinsă pentru a adăuga funcționalități suplimentare.

Rularea aplicatiei cu Docker (in folderul in care se afla Dockerfile)

Construirea imaginii Docker 
```bash
docker build -t <nume>
```
Rularea containerului
```bash
docker run -dp 5011:5011 <nume>
```
Accesarea aplicatiei
Deschidem browserul la [http://localhost:8020]
Descriere Dockerfile

Acest proiect folosește Docker pentru a crea un container izolat ce rulează aplicația Flask. Dockerfile-ul conține pașii următori:

1. **Imagine de bază**: Folosim `python:3.10-alpine` pentru a construi aplicația pe o bază ușoară și eficientă.
2. **Configurarea Flask**: Setăm variabila de mediu `FLASK_APP` pentru a identifica aplicația principală.
3. **Crearea unui utilizator non-root**: Aplicația rulează cu un utilizator non-root (`tari`) pentru siguranță.
4. **Construirea mediului de aplicație**: Creăm un director de lucru și copiem toate fișierele aplicației.
5. **Instalarea dependențelor**: Instalăm pachetele necesare folosind un mediu virtual Python.
6. **Setarea permisiunilor**: Asigurăm permisiuni corecte pentru fișierele statice și scripturile executabile.
7. **Expunerea portului**: Portul 5011 este expus pentru a accesa aplicația.
8. **Pornirea aplicației**: Aplicația este pornită folosind scriptul `dockerstart.sh` și comanda Flask corespunzătoare.

Acest container asigură un mediu curat și izolat, oferind o metodă ușoară de a distribui și rula aplicația Flask pe diferite sisteme.

## Testare

- Testare unitara cu pytest
```bash
pytest app/tests/
```
Explicații pentru fișierul `pytest.ini`

Fișierul **`pytest.ini`** este un fișier de configurare folosit de framework-ul de testare **pytest** pentru a controla comportamentul testelor. Iată o descriere detaliată a fiecărei linii din acest fișier.

1. `pythonpath = .`

- **Explicație:** Acesta setează calea de import pentru pytest, indicând locația principală a proiectului. În acest caz, semnifică faptul că pytest va căuta modulele în directorul curent (`.`), adică rădăcina proiectului.
- **De ce este important:** Permite pytest să acceseze corect modulele și fișierele din proiect, fără a necesita specificarea lor manuală în timpul testării.

2. `testpaths = app/tests`

- **Explicație:** Acesta indică locația directorului care conține testele unitare. În acest caz, pytest va căuta fișierele de testare în directorul `app/tests`.
- **De ce este important:** Acest parametru asigură că pytest va executa doar testele aflate în directorul `app/tests/` și nu va căuta teste în alte locații din proiect.

3. `log_cli = true`

- **Explicație:** Activează logarea la nivel de linie de comandă pentru pytest.
- **De ce este important:** Permite afișarea mesajelor de log în terminal pe măsură ce testele sunt rulate, oferind informații valoroase despre starea testelor (de exemplu, succes, eroare, avertismente).

4. `log_cli_level = DEBUG`

- **Explicație:** Setează nivelul de logare la **DEBUG**, ceea ce înseamnă că pytest va afișa toate mesajele de log, inclusiv cele de tip **debug**, care sunt utile pentru depanare detaliată.
- **De ce este important:** Permite o monitorizare detaliată a testelor și ajută la identificarea și rezolvarea problemelor mai rapid.

5. `log_cli_format = %(asctime)s [%(levelname)-8s] (%(filename)s:%(lineno)s) %(message)s`

- **Explicație:** Acesta definește formatul mesajelor de log afișate de pytest. Fiecare mesaj va include:
  - **`asctime`**: data și ora când a avut loc evenimentul
  - **`levelname`**: nivelul mesajului de log (exemplu: INFO, DEBUG, ERROR)
  - **`filename`** și **`lineno`**: fișierul și linia de cod în care a avut loc evenimentul
  - **`message`**: mesajul propriu-zis
- **De ce este important:** Formatul detaliat ajută la identificarea rapidă a sursei unei probleme sau erori, facilitând depanarea rapidă.

6. `log_cli_date_format = %Y-%m-%d %H:%M:%S`

- **Explicație:** Setează formatul datei și orei afișate în loguri. Formatul specificat este `YYYY-MM-DD HH:MM:SS`.
- **De ce este important:** Formatul clar al datei și orei permite urmărirea cronologică a evenimentelor și erorilor în timpul executării testelor.

Cum ajută aceste setări în procesul de testare:

1. **Organizarea Testelor:** Direcționând pytest să caute testele în directorul specificat (`app/tests`), evităm executarea accidentală a unor fișiere care nu sunt teste.
2. **Monitorizarea detaliată:** Permite logarea la nivel de detaliu complet (prin setarea `DEBUG`) astfel încât să putem observa toate etapele și posibilele erori apărute în timpul rulării testelor.
3. **Formatul personalizat:** Folosind un format detaliat pentru loguri, este mai ușor să urmărești fluxul de execuție al testelor și să identifici rapid problemele.

Aceste configurări sunt esențiale pentru a avea o experiență mai eficientă și clară în rularea și monitorizarea testelor în cadrul proiectului tău.

- Testare cu Jenkins
Testele sunt automatizate si vor rula pe Jenkins, folosind fisierul Jenkinsfile pentru a configura pipeline-ul.
Pornirea serverului de Jenkins
```bash
jenkins
```
Configurare proiect Jenkins
![Structura](/static/1.png)
![Structura](/static/2.png)
![Structura](/static/3.png)

Descriere Jenkinsfile

Acest **Jenkinsfile** configurează pipeline-ul pentru integrarea continuă (CI) și livrarea continuă (CD) a aplicației Flask.

1. **Etapa 'Build'**: Construiește imaginea Docker utilizând Dockerfile-ul din proiect și etichetează imaginea cu numărul curent al build-ului.
2. **Etapa 'pylint - calitate cod'**: Verifică calitatea codului sursă folosind pylint pentru a se asigura că nu există erori de stil sau probleme majore în cod.
3. **Etapa 'Unit Testing cu pytest'**: Rulează testele unitare pentru a verifica funcționalitatea aplicației.
4. **Etapa 'Deploy'**: Creează imaginea Docker pentru aplicația curentă.
5. **Etapa 'Running'**: Rulează containerul Docker creat în etapa anterioară și pune aplicația la dispoziție pe portul 8020.
6. **Secțiunea 'post'**: Oferă curățare pentru a opri și elimina orice container rămas activ.

Acest pipeline permite crearea și testarea automată a aplicației în fiecare build, asigurându-se că aplicația este mereu într-o stare funcțională și disponibilă.



