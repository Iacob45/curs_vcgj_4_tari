============================================================
                        DESCRIEREA APLICAȚIEI
============================================================

Aplicația realizată este o aplicație web construită cu ajutorul framework-ului Flask,
care oferă un API simplu prin care utilizatorii pot accesa informații esențiale despre Brazilia.
Aceasta include:
  - o descriere generală a țării
  - numele capitalei
  - informații despre steagul național


============================================================
                  STRUCTURA LOGICĂ A APLICAȚIEI
============================================================

Aplicația definește trei rute principale:

  • /brazilia           – returnează o descriere generală a Braziliei
  • /brazilia/capitala  – returnează numele capitalei
  • /brazilia/steag     – oferă informații despre steagul național

Logica pentru fiecare răspuns este separată în fișierul auxiliar:
  >> biblioteca_brazilia.py

Acesta conține următoarele funcții:

  → descriere_brazilia()
  → capitala_brazilia()
  → steag_brazilia()

Aceste funcții sunt apelate în fișierul principal:
  >> tari.py

Acest fișier gestionează rutele, apelează funcțiile din bibliotecă și
formează punctul de intrare pentru aplicația Flask.

