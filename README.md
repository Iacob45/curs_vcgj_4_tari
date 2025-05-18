##Autor: Miron Andrei Auras

## Cuprins

- Funcționalitate implementată
- Flux Git și integrare
- Rulare locală
- Rulare cu Docker
- Testare cu Pytest
- Testare automată cu Jenkins

---

## Funcționalitate implementată

Modulul `app/lib/biblioteca_vatican.py` definește trei funcții care oferă informații despre Vatican:

- `descriere_vatican()` – returnează o descriere generală a statului Vatican în format HTML.
- `capitala_vatican()` – oferă informații despre capitală.
- `steag_vatican()` – returnează imaginea drapelului Vaticanului.

Aceste funcții sunt utilizate în fișierul principal Flask `tari.py`, care mapează fiecare funcționalitate la o rută HTTP de tip GET.

#Flux Git și integrare

Am dezvoltat initial in branch-ul special devel_miron_andrei pentru a testa si depana. Stadiul final al proiectului a fost incarcat/copiat pe branch-ul princiapl main_miron_andrei printr-un pull request.

#Rulare locală

bash: source activeaza_venv
bash: source ruleaza_aplicatia

Aplicația va rula la adresa: http://127.0.0.1:5011/vatican

#Rulare cu Docker

-Construirea imaginii Docker:
bash: sudo docker build -t tari:v04 .

-Rularea containerului pe portul 8020:
bash: sudo docker run --name tari -p 8020:5011 tari:v04

Acces aplicație: http://localhost:8020/vatican


#Testare cu Pytest

Testele pentru funcțiile din biblioteca_vatican.py sunt scrise în app/tests/test_biblioteca_vatican.py. Se verifică dacă output-ul HTML al fiecărei funcții este exact cel așteptat.

Comandă de testare:

bash: pytest
bash: flask test


#Testare automată cu Jenkins

Testarea automată a fost realizată cu Jenkins, folosind un pipeline structurat în 5 etape, configurat în fișierul Jenkinsfile.
Etape pipeline:

    Build – Configurarea mediului de lucru, activare .venv și instalare dependințe.

    Unit testing – Rulare flask --app tari test, care declanșează testele definite în pytest.

    Deploy – Construire imagine Docker cu etichetă versiune.

    Running – Pornirea aplicației într-un container Docker, cu mapare port 8020 → 5011.

