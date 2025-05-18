## JAPONIA - Dima Cosmin Ilie

Status implementare: Funcționalitate completă, testată și integrată în branch-ul principal `main_dima_cosmin`.

## Cuprins

- [Descriere functionalitati](#Descriere-functionalitati)
- [Flux Git & Pull Request](#Flux-Git-&-Pull-Request)
- [Detalii implementare](#Detalii-implementare)
- [Rulare locală](#Rulare-locală)

 

## Descriere functionalitati

Am adăugat suport pentru Japonia în aplicație, prin implementarea a trei funcționalități de bază:

    descriere_japonia() – O scurtă descriere a Japoniei

    capitala_japonia() – Returnează numele capitalei Japoniei

    steag_japonia() – Afișează imaginea drapelului Japoniei

Aceste funcționalități sunt accesibile prin următoarele rute Flask:

    GET /japonia – Descriere generală a Japoniei

    GET /japonia/capitala – Numele capitalei

    GET /japonia/steag – Imaginea steagului

Funcțiile sunt implementate în fișierul app/lib/biblioteca_japonia.py și sunt integrate în aplicația principală.

## Flux Git & Pull Request

Pentru dezvoltarea acestei funcționalități, am folosit următorul flux de lucru:

    1.Branch de dezvoltare: Codul a fost dezvoltat pe branch-ul devel_dima_cosmin.

    2.Pull Request: Am creat un Pull Request pentru integrarea modificărilor din devel_dima_cosmin în main_dima_cosmin, pentru a valida integritatea codului și pentru a simula procesul de integrare.

## Detalii implementare

Funcțiile pentru Japonia au fost adăugate în fișierul app/lib/biblioteca_japonia.py. Aplicația principală (tari.py) definește rutele care răspund la cererile GET, oferind utilizatorilor informațiile despre Japonia.

## Rulare locala

Pentru a testa aplicația pe mașina ta locală, urmează pașii de mai jos:

    1.Clonează repository-ul și comută pe branch-ul corespunzător:
    
```bash
mkdir proiect_SCC
cd proiect_SCC
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_dima_cosmin
```
    2.Activează mediul virtual și rulează aplicația:
    
```bash
source activeaza_venv
source ruleaza_aplicatia
```
