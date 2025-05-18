FROM python:3.10-alpine

ENV FLASK_APP tari


#3.8 alpine
RUN adduser -D tari

RUN mkdir -p /home/monica/proiect_scc/curs_vcgj_4_tari
RUN chown -R tari /home/monica/proiect_scc


WORKDIR /home/monica/proiect_scc/curs_vcgj_4_tari

COPY app/ app/
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY requirements.txt requirements.txt
COPY tari.py tari.py
COPY static/ static/

RUN chmod -R 777 static/
RUN chmod +x dockerstart.sh

USER tari

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
