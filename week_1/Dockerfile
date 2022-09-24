FROM python:latest AS build
RUN apt-get update
RUN apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
ADD main.py /
RUN python main.py