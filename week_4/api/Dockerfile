FROM python:latest
RUN pip3 install flask
VOLUME /app
WORKDIR /app
EXPOSE ${API_PORT}
CMD ["python", "api.py"]
