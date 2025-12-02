FROM python:latest

WORKDIR /code

COPY hello.py .

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y

RUN python3 -m pip install -r requirements.txt

CMD python3 hello.py

