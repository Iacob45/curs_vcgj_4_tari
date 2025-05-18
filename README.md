**Proiect SCC – Danemarca**

**Dezvoltator: Marcu Răzvan-Daniel**

---

**Descriere:**
---
În cadrul cursului Servicii de cloud şi containerizare, se va realiza proiectul pentru tema “Ţări” prin implementarea unor tehnologii, precum: Flask, Docker, Jenkins şi GitHub.

---

**Obiectivul proiectului:**
---
Realizarea unei aplicaţii web pentru Danemarca, care conţine trei endpoint-uri: `/danemarca`, `/danemarca/capitala`, `/danemarca/steag`.  
Folosind Flask, vor fi afişate informaţii corespunzătoare fiecărui endpoint. De asemenea, proiectul cuprinde o parte dedicată testării automate prin intermediul Jenkins, iar secţiunea dedicată containerizării se va realiza prin Docker.

---

**Platforme şi tehnologii aplicate:**
---
- **Flask**: Framework Python pentru dezvoltarea aplicaţiei web  
- **GitHub**: Permite gestionarea codului sursă şi a versiunilor în cadrul unei echipe  
- **Docker**: Permite rularea aplicaţiei în containere, asigurând un mediu izolat şi reproductibil  
- **Jenkins**: Automatizează testarea şi livrarea continuă

---

**Setare aplicaţie local:**
---
1. Configurare Git:
```bash
git config --global user.name "username"
git config --global user.email "email"
```

2. Clonare repository:
```bash
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_marcu_razvan
```

3. Activare venv și rulare aplicație:
```bash
source activeaza_venv
source ruleaza_aplicatia
```

---

**Conţinutul proiectului:**
---
Pentru crearea directoarelor și fișierelor:
```bash
mkdir
touch
```

---

**Descrierea generală a fişierului `tari.py`:**
---
Fișierul `tari.py` configurează aplicația Flask și definește rutele accesibile prin metoda HTTP GET:

- `/danemarca` → `index()` și `descriere_danemarca()`
- `/danemarca/capitala` → `capitala()` și `capitala_danemarca()`
- `/danemarca/steag` → `steag()` și `steag_danemarca()`

---

**Containerizarea aplicației folosind Docker:**
---
1. Creare imagine Docker:
```bash
sudo docker build -t tari:v01 .
```

2. Rulare container:
```bash
sudo docker run --name tari -p 8020:5011 tari:v01
```

3. Accesare aplicație:
```text
http://127.0.0.1:8020/danemarca
```

---

**Prezentare Dockerfile:**
---
1. Imagine de bază:
```dockerfile
FROM python:3.10-alpine
```

2. Setare aplicație:
```bash
ENV FLASK_APP=tari
```

3. Utilizator non-root  
4. Structurare spațiu lucru  
5. Instalare dependențe  
6. Permisiuni fișiere  
7. Expunere port:
```dockerfile
EXPOSE 5011
```

8. Pornire server Flask:
```bash
./dockerstart.sh
```

---

**Testarea cu pytest:**
---
Se testează funcțiile Flask și se afișează rezultatul:

- `PASS` – test valid
- `FAIL` – test nereușit

---

**Testare cu pylint:**
---
Analiza codului pentru stil și bune practici.

---

**Jenkins:**
---
1. Verificare și pornire Jenkins:
```bash
systemctl status Jenkins
jenkins
```

2. Acces Jenkins:
```text
localhost:8080
```

**Etapele pipeline-ului (Jenkinsfile):**
- **Build** – creează imagine Docker
- **Pylint** – verifică stilul codului
- **Pytest** – rulează testele unitare
- **Deploy** – construiește imaginea finală
- **Running** – pornește aplicația pe portul 8020

---

**GitHub şi Pull Request:**
---
Proiectul a fost dezvoltat în `devel_marcu_razvan`, testat cu `pytest` și `Jenkins`. Evaluarea a fost făcută prin:

```text
PR #23 - Test PR 1
PR #22 - Actualizare aplicaţie 2
```
