FROM python:latest
RUN pip3 install flask
RUN pip3 install requests
VOLUME /app
WORKDIR /app
EXPOSE ${CONSUMER_PORT}
CMD ["python", "consumer.py"]
