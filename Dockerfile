FROM python:3.11

WORKDIR  /workdir

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt
