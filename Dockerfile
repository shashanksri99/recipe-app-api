FROM python:3.7-alpine
MAINTAINER PlanMyTax

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
#for running in company use the following proxy otherwise comment it and use the run below it
RUN pip install --proxy=10.112.50.97:8080 -r /requirements.txt

#RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
