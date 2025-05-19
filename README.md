# „Info Romania” — Serviciu Web cu Flask 🇷🇴

Un serviciu web simplu, realizat în Python cu Flask, care afișează informații despre România: descriere generală, capitală și drapel.



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
* **Capitală** – afișează „București”
* **Tricolor** – afișează imaginea drapelului României



## STRUCTURĂ

```text
ProjectRoot/
│
├── tari.py                 # Flask app cu rutele HTTP
├── quickrequirements.txt   # Lista pachetelor Python
├── pytest.ini              # Configurații pytest
├── Jenkinsfile             # Pipeline: build, lint, test, deploy, run
├── Dockerfile              # Instrucțiuni Docker
├── dockerstart.sh          # Entrypoint pentru container
├── activeaza_venv          # Script venv local
├── activeaza_venv_jenkins  # Script venv Jenkins
├── ruleaza_aplicatia       # Script pornire server local
├── static/                 # Resurse statice
│   └── romania_flag.jpg    # Imagine drapel
└── app/                    # Codul organizațional
    ├── lib/                # Biblioteci interne
    │   ├── biblioteca_romania.py   # Generare text Romania
    │   └── biblioteca_header.py    # Generare header HTML
    └── tests/              # Teste unitare
        ├── test_biblioteca_romania.py
        └── test_biblioteca_header.py
```



## PREGĂTIRE MEDIU

1. Clonare repo:

```bash
git clone [https://github.com/Iacob45/curs\_vcgj\_4\_tari.git](https://github.com/Iacob45/curs_vcgj_4_tari.git)
cd curs\_vcgj\_4\_tari
```

2. Creare & activare virtualenv:
   ```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3. Instalare dependențe:

```bash
pip install -r quickrequirements.txt
```


## RULARE LOCALĂ
Pornire server Flask pe portul **5011**:
```bash
bash ruleaza_aplicatia
````

Acces: `http://localhost:5011/romania`


## DOCKER

* Construire imagine:
```bash
docker build -t info-romania .
```

* Rulare container:
```bash
docker run -d -p 5011:5011 info-romania
```



## RUTE DISPONIBILE

* **GET** `/romania`        → descriere generală
* **GET** `/romania/capitala` → capitala (București)
* **GET** `/romania/steag`     → afișare drapel

Fiecare pagină include butoane de navigare create de `biblioteca_header`.



## TESTARE

* Testează biblioteca principală:

```bash
export PYTHONPATH=.
pytest app/tests/test\_biblioteca\_romania.py
```

* Testează header:
```bash
export PYTHONPATH=.
pytest app/tests/test_biblioteca_header.py
```

* Pentru ambele simultan:

```bash
pytest
```



## LINT ȘI CALITATE
Verifică stilul codului cu pylint:
```bash
pylint --exit-zero $(find app/lib -name '*.py')
pylint --exit-zero $(find app/tests -name '*.py')
pylint --exit-zero tari.py
````



## CI/CD (Jenkins)

**Jenkinsfile** realizează:

* *BUILD* – setare venv
* *LINT* – pylint pe librării și teste
* *TEST* – `flask --app tari test`
* *DEPLOY* – build Docker image
* *RUN* – rulează containerul



## SCRIPTURI

* **activeaza\_venv**, **activeaza\_venv\_jenkins** – creare + activare venv
* **ruleaza\_aplicatia** – pornire Flask local
* **dockerstart.sh** – activare venv + pornire Flask în Docker



## DEPENDINȚE

* Flask
* pytest
* pylint
* matplotlib
* gunicorn



## LICENȚĂ & CONTRIBUȚII

Licența este definită în fișierul `LICENSE`. Contribuțiile sunt binevenite prin pull request-uri care trec testele și lint-ul.
