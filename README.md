Descrierea aplicatiei

Aplicația realizată este o aplicație web construită cu ajutorul framework-ului Flask, care oferă un API simplu prin care utilizatorii pot accesa informații esențiale despre Brazilia. Aceasta include o descriere generală a țării, numele capitalei și informații despre steagul național.


Structura logică a aplicației

Sunt definite trei rute principale:

  -/brazilia – returnează o descriere generală a Braziliei.

  -/brazilia/capitala – returnează numele capitalei.

  -/brazilia/steag – oferă informații despre steagul național.
  
Iar in biblioteca_brazilia.py se definesc functiile: descriere_brazilia(), capitala_brazilia(), steag_brazilia() pentru o separare logica a continutului. Aceste functii sunt apelate in fisierul principal tari.py.
