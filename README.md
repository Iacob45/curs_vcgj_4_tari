<!-- README gol -->
## ITALIA - Stoica Daria-Andreea

Stadiul implementării: funcționalitate completă, testare finalizată, integrare realizată în branch-ul principal `main_daria_stoica`.

## Cuprins

- [Introducere](#introducere)
- [Structura Modulului Italia](#Structura-Modulului-Italia)
- [Gestionarea Versiunilor și Integrarea Codului](#Gestionarea-Versiunilor-și-Integrarea-Codului)
- [Testare Funcționalitate](#Testare-Funcționalitate)
- [Rulare Locală – Mediu de Dezvoltare](#Rulare-Locală–Mediu-de-Dezvoltare)
- [Containerizare și Executare Izolată](#Containerizare-și-Executare-Izolată)
- [Integrare Continuă cu Jenkins](#Integrare-Continuă-cu-Jenkins)
- [Concluzie](#Concluzie)


1. Introducere
Această lucrare detaliază integrarea componentei dedicate Italiei în cadrul aplicației web realizate cu Flask, în contextul unui proiect colaborativ. Scopul a fost afișarea informațiilor despre Italia într-un mod structurat și accesibil printr-o interfață web, urmând principiile modularității, testabilității și automatizării.

2. Structura Modulului Italia
Funcționalitatea a fost adăugată în fișierul app/lib/biblioteca_italia.py și conține următoarele funcții:

descriere_italia() – întoarce o descriere generală (HTML);

capitala_italia() – returnează numele capitalei;

steag_italia() – furnizează drapelul național.

Acestea sunt apelate prin rute definite în aplicația principală (tari.py), astfel:

Rută Flask	Tip HTTP	Funcție apelată
/italia	GET	descriere_italia()
/italia/capitala	GET	capitala_italia()
/italia/steag	GET	steag_italia()

3. Gestionarea Versiunilor și Integrarea Codului
3.1 Ramuri și dezvoltare locală
Funcționalitatea a fost dezvoltată pe ramura devel_stoica_daria. După finalizarea și validarea codului, s-a creat un Pull Request către main_stoica_daria.


4. Testare Funcționalitate
4.1 Testare unitară
Am utilizat pytest pentru a testa funcțiile definite. Testele se află în app/tests/test_biblioteca_italia.py.

Comanda utilizată:

bash
Copy
Edit
pytest
Rezultatul a fost pozitiv pentru toate cazurile de test.

4.2 Analiza calității codului
Pentru analiza statică, a fost folosit pylint, cu următoarea comandă:

bash
Copy
Edit
pylint tari.py
Scorul obținut a confirmat respectarea convențiilor PEP8 și absența erorilor semnificative.

5. Rulare Locală – Mediu de Dezvoltare
Pașii pentru rularea aplicației local:

Clonare și checkout:

bash
Copy
Edit
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_stoica_daria
Activare și rulare:

bash
Copy
Edit
source activeaza_venv
source ruleaza_aplicatia
Aplicația va fi disponibilă la:
http://127.0.0.1:5011/italia

6. Containerizare și Executare Izolată
6.1 Crearea imaginii
Fișierul Dockerfile creează mediul izolat cu Flask și aplicația:

bash
Copy
Edit
sudo docker build -t tari:v04 .
6.2 Rulare container
bash
Copy
Edit
sudo docker run --name tari -p 8020:5011 tari:v04
Aplicația devine accesibilă la:
http://localhost:8020/italia

7. Integrare Continuă cu Jenkins
7.1 Configurare pipeline
Am utilizat Jenkins pentru testare automată. Etapele pipeline-ului definite în Jenkinsfile:

Build – crearea mediului virtual

pylint – evaluarea calității codului

pytest – testare funcțională

Deploy Docker – creare imagine

Run – lansare container pe portul 8020

7.2 Execuție
După configurare, testarea este declanșată cu opțiunea Build în interfața Blue Ocean. Rezultatul: toate etapele au fost finalizate cu succes (PASS).

8. Concluzie
Integrarea Italiei a fost realizată cu succes, respectând cerințele arhitecturale și funcționale ale proiectului. Funcționalitatea este testată, documentată și implementată conform standardelor moderne de dezvoltare software colaborativă.


