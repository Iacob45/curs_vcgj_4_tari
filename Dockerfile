FROM python:3.10-alpine

ENV FLASK_APP=tari

RUN adduser -D tari
RUN mkdir -p /home/user/SCC2/curs_vcgj_4_tari/
RUN chown -R tari /home/user/SCC2/

WORKDIR /home/user/SCC2/curs_vcgj_4_tari/

COPY app/ app/
COPY static/ static/
COPY tari.py .
COPY dockerstart.sh .
COPY pytest.ini .
COPY quickrequirements.txt .

RUN chmod -R 777 static
RUN chmod +x dockerstart.sh

USER tari

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]