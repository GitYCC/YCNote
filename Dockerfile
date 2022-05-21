FROM python:2.7.9

COPY requirements.txt ./

RUN pip install setuptools==18.5

RUN pip install -r requirements.txt

