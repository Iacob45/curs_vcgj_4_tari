<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Proiect SCC – Danemarca</span>  
Dezvoltator: Marcu Răzvan-Daniel

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Descriere:</span>  
În cadrul cursului Servicii de cloud şi containerizare, se va realiza proiectul pentru tema “Ţări” prin implementarea unor tehnologii, precum: Flask, Docker, Jenkins şi GitHub.

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Obiectivul proiectului:</span>  
Realizarea unei aplicaţii web pentru Danemarca, care conţine trei endpoint-uri:  
`/danemarca`, `/danemarca/capitala`, `/danemarca/steag`  
Folosind Flask, vor fi afişate informaţii corespunzătoare fiecărui endpoint.  
Proiectul include testare automată prin Jenkins și containerizare cu Docker.

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Platforme şi tehnologii aplicate:</span>  
- **Flask**: Framework Python pentru dezvoltarea aplicaţiei web  
- **GitHub**: Gestionarea codului sursă şi a versiunilor  
- **Docker**: Rulare în containere, mediu izolat  
- **Jenkins**: Automatizare testare și livrare continuă

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Setare aplicaţie local:</span>

**1. Configurare Git:**
```bash
git config --global user.name "username"
git config --global user.email "email"
```

**2. Clonare repository în directorul local:**
```bash
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_marcu_razvan
```

**3. Activare venv şi rularea aplicaţiei:**
```bash
source activeaza_venv
source ruleaza_aplicatia
```

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Structura proiectului:</span>  
Pentru a crea directoarele și fișierele s-au folosit:
```bash
mkdir
touch
```

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Descrierea fișierului `tari.py`:</span>  
Fișierul `tari.py` configurează aplicația Flask și definește rutele HTTP pentru informații despre Danemarca:

- `/danemarca` – descriere generală  
- `/danemarca/capitala` – informații despre Copenhaga  
- `/danemarca/steag` – descriere steag

Funcțiile implementate:
```python
descriere_danemarca()
capitala_danemarca()
steag_danemarca()
```

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Containerizarea aplicației folosind Docker:</span>  

**1. Crearea imaginii Docker:**
```bash
sudo docker build -t tari:v01 .
```

**2. Rulare container:**
```bash
sudo docker run --name tari -p 8020:5011 tari:v01
```

**3. Acces aplicație în browser:**
```text
http://127.0.0.1:8020/danemarca
```

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Prezentare Dockerfile:</span>  

1. Imagine de bază:
```dockerfile
FROM python:3.10-alpine
```

2. Setare aplicație Flask:
```bash
ENV FLASK_APP=tari
```

3. Rulare cu utilizator non-root  
4. Structurare workspace  
5. Instalare dependențe în mediu virtual  
6. Setare permisiuni  
7. Expunere port:
```dockerfile
EXPOSE 5011
```

8. Pornire server Flask:
```bash
./dockerstart.sh
```

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Testarea cu pytest:</span>  
Pentru validarea funcționalității se folosesc teste `pytest`. Rezultatul va fi `PASS` sau `FAIL`.

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Testare cu pylint:</span>  
Se analizează stilul și calitatea codului Python.

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">Jenkins:</span>  

**1. Pornire server Jenkins:**
```bash
systemctl status Jenkins
jenkins
```

**2. Acces Jenkins:**
```text
http://localhost:8080
```

**Etapele pipeline-ului definit în Jenkinsfile:**

- **Build**: creare imagine Docker  
- **pylint**: verificare calitate cod  
- **pytest**: rulare teste  
- **Deploy**: construire imagine finală  
- **Running**: rulare container pe portul 8020

---

<span style="font-size:16px; font-family:'Times New Roman'; font-weight:bold;">GitHub şi Pull Request:</span>  

Proiectul a fost dezvoltat în branch-ul `devel_marcu_razvan` și testat local cu `pytest` și `Jenkins`.

**Pull Request-uri proprii:**
```text
PR #23 - Test PR 1
```

**Pull Request-uri efectuate:**
```text
PR #22 – Actualizare aplicaţie 2
```

