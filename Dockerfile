ROM python:3.10-alpine

# Creăm utilizatorul
RUN adduser -D tari

# Ne logăm ca utilizator non-root
USER tari

# Setăm directorul de lucru
WORKDIR /home/tari/

# Copiem toate fișierele necesare
COPY app/ app/
COPY main.py main.py
COPY quickrequirements.txt quickrequirements.txt

# Instalăm dependențele
RUN pip install --upgrade pip
RUN pip install -r quickrequirements.txt

# Expunem portul pe care va rula aplicația
EXPOSE 5050

# Pornim aplicația cu uvicorn
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "5050"]