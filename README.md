# Proiect SCC - Țări: Spania

## Autor
**Balan Carla**  
Branch: `devel_balan_carla`  
Tema: Spania

## Descriere generală
Această aplicație simplă dezvoltată cu Flask este parte din proiectul colaborativ al grupei 444D, tema „Țări”.  
Fiecare student a implementat o funcționalitate legată de o țară. Eu am ales **Spania**.

## Funcționalitate implementată
În acest branch am adăugat:

- Fișierul `app/lib/biblioteca_spania.py` cu două funcții:
  - `capitala_spania()` – afișează capitala Spaniei.
  - `steag_spania()` – afișează descrierea steagului Spaniei.
  
- Trei rute noi în fișierul `app/444D_tari.py`:
  - `/spania` – pagină principală pentru Spania.
  - `/spania/capitala` – afișează capitala.
  - `/spania/steag` – afișează detalii despre steag.

## Stadiu dezvoltare
- ✅ Funcționalitate implementată
- ✅ Cod adăugat în branch `devel_balan_carla`
- ⏳ Pull Request către `main` în curs
- ✅ Cod revizuit de coleg: `@alt_user`
- ✅ Codul testat manual și în Jenkins
- ✅ Dockerfile creat pentru rularea aplicației

## Testare
- ✅ Testare manuală în browser
- ✅ Teste automate scrise în `app/tests/test_biblioteca_spania.py`
- ✅ Rulate cu succes în Jenkins
- ✅ Fișier `Jenkinsfile` adăugat și funcțional

## Containerizare
- ✅ `Dockerfile` creat pentru aplicația cu Spania
- ✅ Imagine Docker construită local
- ✅ Container pornit local
- ✅ Accesat cu succes din browser (`localhost:5000/spania`)

### Capturi de ecran:
1. Imagine Docker creată:
   ![docker-image](docs/spania_docker_build.png)

2. Rulare container și acces din browser:
   ![docker-container](docs/spania_browser_access.png)

3. Mesaje din terminal la pornirea containerului:
   ![docker-terminal](docs/spania_terminal_output.png)

## Review-uri efectuate
- ✅ PR review pentru `@coleg_x` - ID: #12
- ✅ PR review pentru `@coleg_y` - ID: #17

## Ce mai este de făcut
- Integrare finală în `main` după aprobarea PR-ului
- Eventuală încărcare imagine pe DockerHub (opțional)

---

## Resurse
- Repository principal: [curs_vcgj_4_tari](https://github.com/Iacob45/curs_vcgj_4_tari)
- Branch curent: `devel_balan_carla`

