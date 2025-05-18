# Proiect SCC - Țări: Spania

## Autor
**Balan Carla**  
Tema: Spania

## Descriere generală
Tema comună a grupei 444D este "Țări", iar eu mi-am ales țara "Spania".  

## Funcționalitate implementată
În acest branch am adăugat:

- Fișierul `app/lib/biblioteca_spania.py` cu trei funcții:
  - `capitala_spania()` – afișează capitala Spaniei.
  - `steag_spania()` – afișează o imagine cu steagul Spaniei.
  - `descriere_spania()` – oferă o scurtă descriere a Spaniei.

- Patru rute noi în fișierul `app/444D_tari.py`:
  - `/spania` – pagină principală pentru Spania.
  - `/spania/capitala` – afișează capitala.
  - `/spania/steag` – afișează steagul.
  - `/spania/descriere` – oferă o descriere generală a țării.

- Fișierul `app/tests/test_biblioteca_spania.py` conține testele automate pentru funcțiile definite.

## Stadiu dezvoltare
- Funcționalitate implementată
- Cod adăugat în branch `devel_balan_carla`
- Pull Request către `main` în curs
- Cod testat manual și automat
- Dockerfile creat
- Jenkinsfile adăugat

## Testare manuală în browser
Am creat un director in home pe masina virtuala Linux, numit proiect_scc; in el am clonat repository-ul curs_vcgj_4_tari, folosind comanda 
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
iar mai apoi cu comanda 
git checkout devel_balan_carla 
se trece pe branch-ul pe care se va face proiectul.
Dupa dezvoltarea aplicatiei vor incepe testele. Primul va fi testarea in browser prin activarea mediului virtual cu comenzile
source activeaza_venv
source ruleaza_aplicatia
iar mai apoi se acceseaza pe firefox pe http://127:0.0.1:5011 cele trei pagini. 

## Testare cu pytest în mediu virtual
Cu mediul virtual activat folosim comanda 

## Testare cu pylint
...

## Testare cu Jenkins
...

## Testare cu Docker
...

## Ce mai este de făcut
...

## Resurse
- Repository: [https://github.com/Iacob45/curs_vcgj_4_tari](https://github.com/Iacob45/curs_vcgj_4_tari)
- Branch: `devel_balan_carla`

