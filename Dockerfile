FROM python:3.7

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD app.py /app
ADD test_app.py /app
ADD ssh_certificate_generator.py /app
ADD generate_ca_key.py /app

RUN python generate_ca_key.py
RUN chmod 600 ca.key

EXPOSE 3000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]
