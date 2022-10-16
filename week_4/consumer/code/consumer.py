from flask import Flask, redirect, url_for, request, render_template
import json
import os
app = Flask(__name__)

os.environ['CONSUMER_ENDPOINT'] = 'meal_recommendation'
consumer_endpoint = os.environ.get('CONSUMER_ENDPOINT')
@app.route('/' + consumer_endpoint)
def home():
   api_host = os.environ.get('API_HOST')
   api_port = os.environ.get('API_PORT')
   api_endpoint = os.environ.get('API_ENDPOINT')
   url = f"https://{api_host}:{api_port}/{api_endpoint}"
   data = request.GET.get(url)
   result = json.loads(data)
   return render_template('index.html', result)  
if __name__ == '__main__':
   port = os.environ.get('CONSUMER_PORT')
   app.run(host='0.0.0.0', debug=True, port=port)

      