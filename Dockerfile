# Imagine de bază
FROM python:3.12-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele în container
COPY . .

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul pe care rulează Flask
EXPOSE 5000

# Setează variabilele de mediu necesare pentru Flask
ENV FLASK_APP=app/main.py
ENV PYTHONPATH=/app

# Comanda de pornire a aplicației
CMD ["flask", "run", "--host=0.0.0.0"]
