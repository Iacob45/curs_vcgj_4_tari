## JAPONIA - Dima Cosmin Ilie

Stadiul implementării: funcționalitate completă, testare finalizată, integrare realizată în branch-ul principal `main_dima_cosmin`.

## Cuprins

- [Element adăugat](#element-adăugat)
- [Flux de lucru Git și Pull Request-uri](#Flux-de-lucru-Git-și-Pull-Request-uri)
- [Integrare și colaborare GitHub](#Integrare-și-colaborare-GitHub)
  - [Pull Request-uri proprii](#Pull-Request-uri-proprii)
  - [Review-uri efectuate](#Review-uri-efectuate)
- [Implementare funcționalitate](#implementare-funcționalitate)
- [Rulare locală a aplicației](#rulare-locală-a-aplicației)

## Element adăugat

Am integrat funcționalitatea corespunzătoare țării **Japonia** în aplicația software dezvoltată la nivelul grupei.

## Implementare funcționalitate

Am implementat funcțiile specifice elementului adăugat în `app/lib/biblioteca_japonia.py` care vor afișa informațiile necesare descrierii generale a țării:

- `descriere_japonia()`
- `capitala_japonia()`
- `steag_japonia()`

Aplicația principală, `tari.py`, definește 3 rute implementate cu ajutorul framework-ului Flask, accesibile prin metoda HTTP `GET`, fiecare returnând conținut HTML generat de funcțiile de mai sus. Fiecare rută corespunde unei componente informaționale distincte.

- `GET /japonia` – punct de intrare general care oferă o descriere pe scurt a Japoniei;
- `GET /japonia/capitala` – returnează numele capitalei Japoniei;
- `GET /japonia/steag` – returnează drapelul Japoniei.

Modulul a fost integrat în aplicația existentă astfel încât să respecte arhitectura propusă și să poată fi extins ușor cu funcționalități suplimentare.

## Flux de lucru Git și Pull Request-uri

Pentru dezvoltarea funcționalității, am utilizat un flux de lucru organizat pe ramuri (branch-uri), care respectă bunele practici de colaborare GitHub.

Inițial, am implementat codul în branch-ul personal de dezvoltare: `devel_dima_cosmin`. După ce funcționalitatea a fost testată local, analizată cu `pylint` și validată prin teste cu `pytest` și Jenkins, codul a fost integrat progresiv:

 **PR intern** – am realizat un *Pull Request* de la `devel_dima_cosmin` către `main_dima_cosmin` pentru a valida integritatea codului meu și a simula procesul de integrare.

## Rulare locală a aplicației

Pentru a putea testa funcționalitatea adăugată, aplicația poate fi rulată local, într-un mediu virtual Python `(.venv)`.

1. Se clonează repository-ul și se accesează branch-ul de dezvoltare corespunzător:

```bash
mkdir proiect_SCC
cd proiect_SCC
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_dima_cosmin
```

2. Se activează venv în directorul curent și se rulează aplicația, urmând a fi accesată în browser la adresa 127.0.0.1:5011/japonia:

```bash
source activeaza_venv
source ruleaza_aplicatia
```



