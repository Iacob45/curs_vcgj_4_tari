
# „Info Andorra” — Serviciu Web cu Flask 🇦🇩

Un serviciu web simplu, realizat în Python cu Flask, care afișează informații despre Andorra: descriere generală, capitală și drapel.

## INDEX

* INTRODUCERE
* STRUCTURĂ
* PREGĂTIRE MEDIU
* RULARE LOCALĂ
* DOCKER
* RUTE DISPONIBILE
* TESTARE
* LINT ȘI CALITATE
* CI/CD (Jenkins)
* SCRIPTURI
* DEPENDINȚE
* LICENȚĂ & CONTRIBUȚII

## INTRODUCERE

Serviciul expune trei pagini HTML generate din funcții Python:

* **Descriere** – prezentare succintă a țării
* **Capitală** – afișează „Andorra la Vella”
* **Steag** – afișează imaginea drapelului Andorra

## STRUCTURĂ

```text
ProjectRoot/
├── tari.py
├── quickrequirements.txt
├── pytest.ini
├── Jenkinsfile
├── Dockerfile
├── dockerstart.sh
├── static/
│   └── Flag_of_Andorra.png
└── app/
    ├── lib/
    │   ├── biblioteca_andorra.py
    │   └── biblioteca_header.py
    └── tests/
        ├── test_biblioteca_andorra.py
        └── test_biblioteca_header.py
```

## PREGĂTIRE MEDIU

```bash
git clone https://github.com/mosspatron/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r quickrequirements.txt
```

## RULARE LOCALĂ

```bash
bash ruleaza_aplicatia
```

Acces: `http://localhost:5011/andorra`

## DOCKER

```bash
docker build -t info-andorra .
docker run -d -p 5011:5011 info-andorra
```

## RUTE DISPONIBILE

* **GET** `/andorra`         → descriere generală
* **GET** `/andorra/capitala` → capitala
* **GET** `/andorra/steag`     → afișare drapel

## TESTARE

```bash
pytest app/tests/test_biblioteca_andorra.py
pytest app/tests/test_biblioteca_header.py
pytest
```

## LINT ȘI CALITATE

```bash
pylint --exit-zero $(find app/lib -name '*.py')
pylint --exit-zero $(find app/tests -name '*.py')
pylint --exit-zero tari.py
```

## CI/CD (Jenkins)

* BUILD
* LINT
* TEST
* DEPLOY
* RUN

## SCRIPTURI

* activeaza_venv, activeaza_venv_jenkins
* ruleaza_aplicatia
* dockerstart.sh

## DEPENDINȚE

* Flask
* pytest
* pylint
* gunicorn

## LICENȚĂ & CONTRIBUȚII

Licența este în `LICENSE`. Contribuțiile sunt acceptate prin pull request-uri.
