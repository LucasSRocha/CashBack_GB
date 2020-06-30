FROM python:3.8

ENV PYTHONWARNINGS ignore
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -U pip && pip install -r requirements-dev.txt --quiet

WORKDIR /webapps

EXPOSE 8000
