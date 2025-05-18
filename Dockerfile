FROM python:3.10-alpine

ENV FLASK_APP tari


#3.8 alpine
RUN adduser -D tari

RUN mkdir -p /home/carla/Desktop/proiect_scc/curs_vcgj_4_tari
RUN chown -R tari /home/carla/Desktop/proiect_scc


WORKDIR /home/carla/Desktop/proiect_scc/curs_vcgj_4_tari

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY tari.py tari.py
COPY static static

RUN chmod -R 777 static
RUN chmod +x dockerstart.sh

USER tari

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
