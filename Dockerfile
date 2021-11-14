FROM python:2.7.9

COPY requirements.txt ./

RUN pip install -r requirements.txt

