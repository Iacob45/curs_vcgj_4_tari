**Aplicație Flask: Informații despre Honduras**

Această aplicație oferă informații despre Honduras printr-o interfață web simplă bazată pe Flask. Include trei endpoint‑uri care returnează conținut HTML: descriere generală a țării, capitala și imaginea steagului.

--- 

## Cuprins

- I. Structura proiectului
- II. Instalare și configurare
- III. Rulare aplicație
- IV. Endpoint-uri disponibile
- V. Testare
- VI. Controlul calității codului
- VII. CI/CD (Jenkins)
- VIII. Docker
- IX. Scripturi utile
- X. Dependințe externe
- XI. Licență

---

#I. Structura proiectului

```
├── tari.py                      # Fișierul principal al aplicației Flask
├── ruleaza_aplicatia            # Script Bash pentru rularea aplicației
├── quickrequirements.txt        # Lista modulelor externe necesare
├── pytest.ini                   # Configurația pytest
├── Jenkinsfile                  # Pipeline CI/CD (Build, Quality, Test, Deploy, Run)
├── Dockerfile                   # Definiție imagine Docker
├── dockerstart.sh               # Entrypoint pentru container Docker
├── activeaza_venv               # Script de activare venv local
├── activeaza_venv_jenkins       # Script de creare și activare venv în Jenkins
├── LICENSE                      # Licența proiectului
├── README.md                    # Documentația proiectului
├── .gitignore                   # Fișier de excludere Git
├── static/                      # Fișiere statice (imagini, CSS, etc.)
│   └── honduras__42861.jpg      # Steagul Honduras
└── app/                         # Codul aplicației organizat în pachete
    ├── lib/                     # Funcții de generare a conținutului HTML
    │   └── biblioteca_honduras.py
    └── tests/                   # Teste unitare pentru bibliotecă
        └── test_biblioteca_honduras.py
```

---

#II. Instalare și configurare

### 1. Clonare repository

```bash
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
```

### 2. Configurare mediu Python

```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r quickrequirements.txt
```

### 3. Fișier de configurare pentru testing

* `pytest.ini` definește directorul rădăcină și markerii folosiți.

---

#III. Rulare aplicație

### Local

```bash
bash ruleaza_aplicatia
```

### Docker

```bash
docker build -t aplicatie-honduras .
docker run --rm -p 5011:5011 aplicatie-honduras
```

Aplicația va fi disponibilă pe `http://localhost:5011/honduras`

---

#IV. Endpoint-uri disponibile

| Ruta                 | Descriere                                 | Metodă |
| -------------------- | ----------------------------------------- | ------ |
| `/honduras`          | Descriere generală a Honduras             | GET    |
| `/honduras/capitala` | Informații despre capitala Honduras       | GET    |
| `/honduras/steag`    | Afișează steagul Honduras ca imagine HTML | GET    |

Fiecare pagină include linkuri de navigare între endpoint-uri și conținut HTML generat din `app/lib/biblioteca_honduras.py`.

---

#V. Testare

Testele sunt în `app/tests/test_biblioteca_honduras.py` și verifică funcțiile:

- descriere_honduras()
- capitala_honduras()
- steag_honduras()

Rulare teste:

```bash
# PYTHONPATH=. este setat pentru ca toate directoarele si fiserele
# din proiect sa fie vizibile
export PYTHONPATH=.
pytest -v
```

---

#VI. Controlul calității codului

Se folosește `pylint` pentru analiza statică a codului. Pentru a rula:

```bash
pylint app/lib/biblioteca_honduras.py app/tests/test_biblioteca_honduras.py tari.py
```

---

#VII. CI/CD (Jenkins)

Pipeline-ul definit în `Jenkinsfile` conține următoarele etape:

1. **Build** – verifică structura directorului, pornește mediul virtual
2. **Controlul calității** – rulează `pylint` pe toate fișierele relevante
3. **Unit Testing** – rulează `pytest`
4. **Deploy** – creează o imagine Docker marcată cu `BUILD_NUMBER`
5. **Run** – pornește containerul cu portul 8020 mapat la 5011

---

#VIII. Docker

- **Dockerfile**: imagine bazată pe Python 3.10 Alpine, creează utilizator non-root, copiază codul și scripturile, setează permisiuni și rulează aplicația cu entrypointul `dockerstart.sh`.
- **dockerstart.sh**: activează mediul virtual și pornește aplicația cu `flask run` pe `0.0.0.0:5011`

---

#IX. Scripturi utile

dockerstart.sh – entrypoint pentru aplicație în Docker
ruleaza_aplicatia – pornește serverul Flask local
activeaza_venv / activeaza_venv_jenkins – creează și activează mediu virtual pentru local și Jenkins

---

#X. Dependințe externe

- Flask
- pytest
- pylint
- matplotlib
- gunicorn

---

#XI. Licență

Acest proiect este licențiat sub licența MIT definită în fișierul `LICENSE`.