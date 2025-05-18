## ITALIA - Stoica Daria-Andreea

Stadiul implementării: funcționalitate completă, testare finalizată, integrare realizată în branch-ul principal `main_daria_stoica`.

## Cuprins

- [Element adăugat](#element-adăugat)
- [Flux de lucru Git și Pull Request-uri](#Flux-de-lucru-Git-și-Pull-Request-uri)
- [Integrare și colaborare GitHub](#Integrare-și-colaborare-GitHub)
  - [Pull Request-uri proprii](#Pull-Request-uri-proprii)
  - [Review-uri efectuate](#Review-uri-efectuate)
- [Implementare funcționalitate](#implementare-funcționalitate)
- [Rulare locală a aplicației](#rulare-locală-a-aplicației)
- [Rulare aplicație cu Docker](#rulare-aplicație-cu-docker)
- [Testare cu pytest](#testare-cu-pytest)
- [Testare calitate cod cu pylint](#testare-calitate-cod-cu-pylint)
- [Testare automată cu Jenkins](#testare-automată-cu-jenkins)
  - [Etapele testării](#etapele-testării)

## Element adăugat

Funcționalitatea aferentă statului Italia a fost adăugată și integrată în aplicația software realizată de grupă.

## Implementare funcționalitate

Am implementat funcțiile specifice elementului adăugat în `app/lib/biblioteca_italia.py` care vor afișa informațiile necesare descrierii generale a țării:

- `descriere_italia()`
- `capitala_italia()`
- `steag_italia()`

Aplicația principală, `tari.py`, utilizeaza framework-ul Flask pentru a expune aceste funcții prin rute de tip HTTP `GET`, fiecare livrând conținut HTML specific.

- `GET /italia` – oferă o descriere generală;
- `GET /italia/capitala` – returnează capitala Italiei;
- `GET /italia/steag` – returnează drapelul Italiei.

Modulul a fost integrat în structura existentă astfel încât să fie extensibil și să respecte arhitectura proiectului.

## Flux de lucru Git și Pull Request-uri

Pentru dezvoltare, a fost utilizat un model de lucru bazat pe ramuri dedicate, conform bunelor practici GitHub.

Inițial, funcționalitatea a fost dezvoltată în branch-ul `devel_stoica_daria`. După testare locală, verificare cu pylint, rularea testelor pytest și validarea în Jenkins, modificările au fost integrate astfel:

Pull Request intern – realizat de la `devel_stoica_daria` către `main_stoica_daria` pentru a simula și valida procesul de integrare.

Fiecare PR a trecut printr-un proces de review realizat de colegii de grupă, asigurând o integrare sigură și coerentă.
## Integrare și colaborare GitHub

Pentru integrarea finală a funcționalității, s-a respectat fluxul de lucru standard cu Pull Request-uri.

După revizuire și aprobare, Pull Request-ul a fost integrat.

### Pull Request-uri proprii

- PR #9 - Devel stoica daria
- PR #22 - Actualizare aplicatie 2

### Review-uri efectuate

- PR #23 - Test PR 1
- PR #26 - Devel mirescu monica

## Rulare locală a aplicației

Pentru testarea locală a funcționalității, aplicația se rulează într-un mediu virtual (.venv) după parcurgerea pașilor de mai jos:

1. Se clonează repository-ul și se accesează branch-ul de dezvoltare corespunzător:

```bash
mkdir proiect_SCC
cd proiect_SCC
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_stoica_daria
```

2. Se activează venv în directorul curent și se rulează aplicația, urmând a fi accesată în browser la adresa 127.0.0.1:5011/italia:

```bash
source activeaza_venv
source ruleaza_aplicatia
```

## Rulare aplicație cu Docker

Aplicația a fost containerizată cu Docker pentru a permite rularea într-un mediu controlat și portabil. Fișierul Dockerfile conține pașii de configurare, iar scriptul `dockerstart.sh` pornește aplicația.

1. Acest proces presupune crearea unei imagini Docker care include codul aplicației, dependențele Python și configurațiile necesare pentru execuție.

```bash
sudo docker build -t tari:v04 .
```

2. După construirea imaginii, aplicația poate fi rulată într-un container, accesibil local prin browser (portul 5011 este mapat pe 8020). Astfel, indiferent de sistemul de operare sau de configurația locală, funcționalitatea poate fi testată și demonstrată uniform.

```bash
sudo docker run --name tari -p 8020:5011 tari:v04
```


## Testare cu pytest

Folosind framework-ul Python **pytest** am dezvoltat teste unitare, construite pentru a verifica dacă funcțiile `descriere_italia()`, `capitala_italia()` și `steag_italia()` returnează conținutul HTML corespunzător, conform specificațiilor. În cazul trecerii unui test, valoarea returnată va fi PASS, iar în caz contrar FAIL. Fișierul `pytest.ini` controlează testele, direcționând în principal către locația fișierului ce conține testele efective, `app/tests/test_biblioteca_italia.py`.

1. Inițial, se pornește testarea aplicației prin comanda: `pytest`.

2. Rezultatele testelor apar în consolă, indicând PASS/FAIL pentru fiecare caz.

## Testare calitate cod cu pylint

Analiza statică a codului a fost realizată cu `pylint`, pentru a evalua stilul, redundanțele și posibilele erori.

1. Pornirea testării se face prin comanda `pylint tari.py`.

2. La final, se afișează scorul general și eventuale sugestii de îmbunătățire.


## Testare automată cu Jenkins

Pentru integrarea continuă (CI), aplicația a fost configurată în Jenkins, care rulează automat pașii de testare pentru fiecare commit important.

1. Pentru început, se verifică starea serviciului Jenkins și se pornește. Platforma web a utilitarului se accesează local, https://localhost:8080.

```bash
systemctl status jenkins
jenkins
```

2. În interfața web, a fost creat un pipeline care preia automat codul din repository.

3. Apăsând Build, se lansează procesul de testare automată. Rezultatele pot fi urmărite în detaliu prin plugin-ul Blue Ocean.


### Etapele testării

Fișierul `Jenkinsfile` definește următorii pași executați automat în cadrul pipeline-ului:

1. Build
Activează mediul virtual necesar aplicației.

2. pylint-calitate cod
Rulează pylint pe fișierele din `app/lib/`, `app/tests/`, `tari.py`. Erorile nu opresc execuția pipeline-ului.

3. Unit Testing cu pytest
Rulează testele definite, utilizând comanda `flask --app tari test`.

4. Deploy
Construiește o imagine Docker tari:v<ID> unde <ID> este identificatorul rularii curente (${BUILD_NUMBER}).

5. Running
Containerul este lansat în fundal, aplicația rulează și este mapată de pe portul 5011 de pe container pe portul 8020 al gazdei.


