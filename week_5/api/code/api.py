from flask import Flask, jsonify
import psycopg2
import random
import os

# Make this file a minimalist API endpoint that randomly offers a 
# random pick out of 15 meal recommendations along with a price
# The endpoint delivers 1 meal recommendation in JSON format
#Websites I used:
#https://www.postgresqltutorial.com/postgresql-python/connect/
#https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f
#https://www.devopsroles.com/deploy-flask-mysql-app-with-docker-compose/
#https://www.geeksforgeeks.org/postgresql-python-querying-data/#:~:text=The%20fetchone()%20method%20returns,will%20return%20the%20next%20record.

app = Flask(__name__)


os.environ['API_ENDPOINT'] = 'meal'
api_endpoint = os.environ.get('API_ENDPOINT')
@app.route('/' + api_endpoint, methods=['GET'])
def random_meal():
    #create a connection to pyscopg2
    conn = psycopg2.connect( #need these specific variables to connect
    database = os.environ.get('POSTGRES_DB'), #the environmental variables from the .env file
    user = os.environ.get('POSTGRES_USER'),
    password = os.environ.get('POSTGRES_PASSWORD'),
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT')
    )
    #create a cursoer
    cursor = conn.cursor()
    #execute the query
    cursor.execute("SELECT MealName, MealPrice FROM Meals ORDER BY random() LIMIT 1")
    query = cursor.fetchone() 
    result = list(query)
    meal_recommendation = {"meal recommendation": result[0],"price": result[1]}
    cursor.close()
    conn.close()
    return jsonify(meal_recommendation)

     
if __name__ == '__main__':
    port=os.environ.get('API_PORT')
    app.run(host="0.0.0.0", debug=True, port=port )
