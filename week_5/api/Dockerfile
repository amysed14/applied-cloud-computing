FROM python:3.8.2
RUN pip3 install flask
RUN pip3 install psycopg2
VOLUME /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "api.py"]
