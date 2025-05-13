FROM python:3.10-alpine

ENV FLASK_APP tari

RUN adduser -D tari


RUN mkdir -p /home/user/proiect/curs_vcgj_4_tari/
RUN chown -R tari /home/user/proiect/

WORKDIR /home/proiect

COPY app app
COPY tari.py tari.py
COPY requirments.txt requirments.txt
COPY static static
COPY templates templates
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini

RUN chmod -R 777 static
RUN chmod +x dockerstart.sh

USER tari

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirments.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5011"]
 
