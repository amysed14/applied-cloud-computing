from flask import Flask, render_template 
import requests
import json
import os
app = Flask(__name__)

#websites I used
#https://stackoverflow.com/questions/63662801/communication-between-2-flask-apps-in-2-docker-containers
#https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask
#https://blog.hubspot.com/website/html-line-break#:~:text=To%20do%20a%20line%20break%20in%20HTML%2C%20use%20the%20%3Cbr,element%2C%20there's%20no%20closing%20tag.
#https://stackoverflow.com/questions/52664673/how-to-get-port-of-docker-compose-from-env-file


@app.route('/')
def home():
   api_host = os.environ.get('API_HOST')
   api_port = os.environ.get('API_PORT')
   api_endpoint = os.environ.get('API_ENDPOINT')
   url = f'http://{api_host}:{api_port}/{api_endpoint}'
   try:
      response = requests.get(url)
   except requests.ConnectionError:
      return "Connection Error"  
   result = response.json()
   return render_template('index.html',recommendation=result['meal recommendation'], price=result['price'] )  
if __name__ == '__main__':
   port = os.environ.get('CONSUMER_PORT')
   app.run(host="0.0.0.0", debug=True, port=port)
