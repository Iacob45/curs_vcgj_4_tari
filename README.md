# 🇰🇵 Coreea de Nord – Coman Silviu

**Stadiul implementării:** Funcționalitate completă, testare finalizată, integrare realizată în branch-ul principal `main_silviu_coman`.

---

## 🗂️ Cuprins

- [Element adăugat](#element-adăugat)
- [Flux de lucru Git și Pull Request-uri](#flux-de-lucru-git-și-pull-request-uri)
- [Integrare și colaborare GitHub](#integrare-și-colaborare-github)
  - [Pull Request-uri proprii](#pull-request-uri-proprii)
  - [Review-uri efectuate](#review-uri-efectuate)
- [Implementare funcționalitate](#implementare-funcționalitate)
- [Rulare locală a aplicației](#rulare-locală-a-aplicației)
- [Rulare aplicație cu Docker](#rulare-aplicație-cu-docker)
- [Testare cu pytest](#testare-cu-pytest)
- [Testare calitate cod cu pylint](#testare-calitate-cod-cu-pylint)
- [Testare automată cu Jenkins](#testare-automată-cu-jenkins)
  - [Etapele testării](#etapele-testării)

---

## 🆕 Element adăugat

Am integrat funcționalitatea corespunzătoare țării **Coreea de Nord** în aplicația software dezvoltată la nivelul grupei.

---

## 🛠️ Implementare funcționalitate

Am implementat funcțiile specifice elementului adăugat în `app/lib/biblioteca_coreea_de_nord.py`, care vor afișa informațiile necesare descrierii generale a țării:

- `descriere_coreea_de_nord()`
- `capitala_coreea_de_nord()`
- `steag_coreea_de_nord()`

Aplicația principală, `tari.py`, definește 3 rute implementate cu ajutorul framework-ului Flask:

- `GET /coreea_de_nord` – descriere generală;
- `GET /coreea_de_nord/capitala` – numele capitalei;
- `GET /coreea_de_nord/steag` – drapelul țării.

---

## 🔄 Flux de lucru Git și Pull Request-uri

Dezvoltarea s-a realizat în branch-ul `devel_silviu_coman`. După testare locală și verificări cu `pylint`, `pytest` și Jenkins, funcționalitatea a fost integrată prin Pull Request către `main_silviu_coman`.

---

## 🔗 Integrare și colaborare GitHub

- Rezultatele testelor automate au fost atașate în PR.
- PR-ul a fost aprobat și integrat.

### 📝 Pull Request-uri proprii

- PR #10 – Devel silviu coman
- PR #23 – Actualizare aplicație 3

### 🔍 Review-uri efectuate

- PR #24 – Test PR 2
- PR #27 – Devel barbu andreea

---

## 🖥️ Rulare locală a aplicației

```bash
mkdir proiect_SCC
cd proiect_SCC
git clone https://github.com/Iacob45/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
git checkout devel_silviu_coman

source activeaza_venv
source ruleaza_aplicatia
