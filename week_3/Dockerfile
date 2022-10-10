FROM python:3.8.2
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
VOLUME /app
WORKDIR /app
EXPOSE 8000
CMD ["/bin/bash", "-c", "python web/manage.py migrate && python web/manage.py runserver 0.0.0.0:8000"]


#CMD ["python", "web/manage.py", "runserver", "0.0.0.0:8000"] 
#Sites used for assignment
#Used video recording of lecture as well
#https://stackoverflow.com/questions/30063907/docker-compose-how-to-execute-multiple-commands
#https://stackoverflow.com/questions/20858381/what-does-bash-c-do