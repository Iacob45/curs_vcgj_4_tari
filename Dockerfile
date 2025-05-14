# Folosește imaginea oficială Python 3.10 Alpine
FROM python:3.10-alpine

# Setăm variabila de mediu pentru Flask
ENV FLASK_APP=tari

# Creăm utilizatorul non-root
RUN adduser -D tari

# Creăm și setăm calea de lucru pentru aplicație
RUN mkdir -p /home/user/proiect_Cristiana/curs_vcgj_4_tari/
RUN chown -R tari /home/user/proiect_Cristiana/

# Setăm directorul de lucru
WORKDIR /home/user/proiect_Cristiana/curs_vcgj_4_tari/

# Copiem fișierele aplicației
COPY app/ app/
COPY tari.py tari.py
COPY requirements.txt requirements.txt
COPY static/ static/
COPY templates/ templates/
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini

# Setăm permisiunile pentru fișierele de statice
RUN chmod -R 755 static/
RUN chmod +x dockerstart.sh

# Comutăm utilizatorul pentru a lucra cu permisiuni mai mici
USER tari

# Creăm mediul virtual
RUN python3 -m venv .venv

# Instalăm dependențele din requirements.txt
RUN .venv/bin/pip install --upgrade pip
RUN .venv/bin/pip install -r requirements.txt

# Expunem portul pe care va rula aplicația Flask
EXPOSE 5011

# Comanda pentru a porni aplicația Flask
ENTRYPOINT ["./dockerstart.sh"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5011"]

