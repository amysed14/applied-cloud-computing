FROM python:latest
RUN apt-get update -y && \  
   apt-get install -y python3-pip python-dev
RUN pip3 install flask
WORKDIR /app
VOLUME /app
EXPOSE ${CONSUMER_PORT}
CMD ["python", "consumer.py"]
