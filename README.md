
# „Info Kosovo” — Serviciu Web cu Flask 🇽🇰

Un serviciu web simplu, realizat în Python cu Flask, care afișează informații despre Kosovo: descriere generală, capitală și drapel.

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
* **Capitală** – afișează „Prishtina”
* **Steag** – afișează imaginea drapelului Kosovo

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
│   └── Flag_of_Kosovo.png
└── app/
    ├── lib/
    │   ├── biblioteca_kosovo.py
    │   └── biblioteca_header.py
    └── tests/
        ├── test_biblioteca_kosovo.py
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

Acces: `http://localhost:5011/kosovo`

## DOCKER

```bash
docker build -t info-kosovo .
docker run -d -p 5011:5011 info-kosovo
```

## RUTE DISPONIBILE

* **GET** `/kosovo`         → descriere generală
* **GET** `/kosovo/capitala` → capitala
* **GET** `/kosovo/steag`     → afișare drapel

## TESTARE

```bash
pytest app/tests/test_biblioteca_kosovo.py
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
