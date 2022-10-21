FROM python:3.8.2
RUN pip3 install flask
RUN pip3 install requests
VOLUME /app
WORKDIR /app
EXPOSE 80
CMD ["python", "consumer.py"]

