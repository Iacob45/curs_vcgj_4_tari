# Proiect SCC - Țări: Spania

## Autor
**Balan Carla**   
Tema: Spania

## Descriere generală
Tema comuna a grupei 444D este "Tari", iar eu mi-am ales tara "Spania". 

## Funcționalitate implementată
În acest branch am adăugat:

- Fișierul `app/lib/biblioteca_spania.py` cu trei funcții:
  - `capitala_spania()` – afișează capitala Spaniei.
  - `steag_spania()` – afișează o imagine cu steagul Spaniei.
  - `descriere_spania()` – oferă o scurtă descriere a Spaniei.

- Trei rute noi în fișierul `app/444D_tari.py`:
  - `/spania` – pagină principală pentru Spania.
  - `/spania/capitala` – afișează capitala.
  - `/spania/steag` – afișează steagul.
  - `/spania/descriere` – oferă o descriere generală a țării.

## Stadiu dezvoltare
- Funcționalitate implementată
- Cod adăugat în branch `devel_balan_carla`
- Pull Request către `main` în curs
- Cod revizuit de coleg: `@alt_user`
- Codul testat manual și în Jenkins
- Dockerfile creat pentru rularea aplicației

## Testare
- Testare manuală în browser
- Teste automate scrise în `app/tests/test_biblioteca_spania.py`
- Rulate cu succes în Jenkins
- Fișier `Jenkinsfile` adăugat și funcțional

## Containerizare
- `Dockerfile` creat pentru aplicația cu Spania
- Imagine Docker construită local
- Container pornit local
- Accesat cu succes din browser (`localhost:5000/spania`)

