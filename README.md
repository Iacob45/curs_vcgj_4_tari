# **Țară Implementată :** Lituania
# **Dezolvator Proiect : ** Calcan Cristian Nicolae
# Proiect DevOps, virtualizare, containerizare, github, jenkins. 

## Cuprins
- [Contribuții  la Implementare](#Contribuții-la-Implementare)
- [Tehnologii utilizate](#Tehnologii-utilizate)
- [Github](#github)
  - [Github Local Configurare](#Github-Local-Configurare)
  - [PR & Review-uri](#PR--Review-uri)
- [Rulare aplicatie Local](#Rulare-aplicatie-Local)
- [Rulare aplicatie Docker](#Rulare-aplicatie-Docker)
- [Testare cu pytest](#Testare-cu-pytest)
- [Testare cu pylint](#Testare-cu-pylint)
- [Testare cu Jenkins](#Testare-cu-Jenkins)

## Contribuții la Implementare

În cadrul cursului Servicii de cloud şi containerizare, se va realiza proiectul pentru tema “Ţări” prin implementarea unor tehnologii, precum: Flask, Docker, Jenkins şi GitHub.

Am integrat funcționalitatea corespunzătoare țării Lituania în aplicația web dezvoltată în cadrul proiectului de grup. Aplicația include trei endpoint-uri – “/lituania”, “/lituania/capitala” și “/lituania/steag” – fiecare afișând informații specifice. Proiectul este containerizat folosind Docker și include testare automată configurată prin Jenkins dar și scripturile specifice.

In proiect avem functiile specifice celor 3 endpointuri `descriere_lituania(),capitala_lituania,steag_lituania()` care sunt regasite in `app/lib/biblioteca_lituania.py`

Fișierul principal al aplicației, `tari.py`, definește trei rute, implementate folosind framework-ul Flask și accesibile prin metoda HTTP `GET` -> GET `/lituania,/lituania/capitala,/lituania/steag`

## Tehnologii utilizate

- Mașină virtuală Ubuntu – Mediu de dezvoltare și testare configurat pe o distribuție Linux (Ubuntu), utilizat pentru rularea aplicației și a serviciilor.

- Flask – Framework web scris în Python, utilizat pentru dezvoltarea aplicației și definirea endpoint-urilor.

- GitHub – Platformă pentru versionarea codului sursă și colaborarea în echipă.

- Docker – Utilizat pentru containerizarea aplicației, oferind un mediu de rulare izolat și ușor de reprodus.

- Jenkins – Instrument de integrare continuă, folosit pentru automatizarea procesului de testare și livrare a aplicației.
