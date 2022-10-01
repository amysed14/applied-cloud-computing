FROM python:3.10.7
RUN apt-get update && apt-get install wget
RUN pip3 install jupyter
ENV USER user1
RUN useradd -ms /bin/bash ${USER}
USER ${USER}
RUN mkdir /home/${USER}/notebooks
WORKDIR /home/${USER}/notebooks
RUN wget https://raw.githubusercontent.com/amysed14/SCU-Projects/master/data_analytics/FinalProject_MSIS_2607_Fall_2021.ipynb -P /home/${USER}/notebooks
RUN wget https://raw.githubusercontent.com/amysed14/SCU-Projects/master/data_analytics/marketing_campaign.csv -P /home/${USER}/notebooks
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD jupyter notebook --ip=0.0.0.0 --port 8888  

#tutorial/links used:
#September 29th recording
#https://www.youtube.com/watch?v=OlYUgQzTEVU
#https://www.tecmint.com/wget-download-file-to-specific-directory/