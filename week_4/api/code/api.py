from flask import Flask
import random
import json
import os


# Make this file a minimalist API endpoint that randomly offers a 
# random pick out of 15 meal recommendations along with a price
# The endpoint delivers 1 meal recommendation in JSON format

#websites used for api.py
#https://www.codegrepper.com/code-examples/python/python+dict+get+random+key
#https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python

app = Flask(__name__)

os.environ['API_ENDPOINT'] = 'meal'
api_endpoint = os.environ.get('API_ENDPOINT')
@app.route('/' + api_endpoint)
def random_meal():
    meal_choices ={'Fiesta Lime Chicken':'$17.99', 'Hand-Battered Fish & Chips':'$18.29',
                    'Classic Burger':'$8.99', '8oz Top Sirloin':'$25.99', 'Cedar-Grilled Salmon':'$23.59', 
                     'Double-Glazed Baby-Back Ribs':'$17.99', 'Grilled Shrimp Avocado & Grapefruit Salad':'$18.99',
                     '3-Cheese Chicken Cavatappi':'$11.99', 'Tuscan Tomato Bisque':'$9.25', 'Santa Fe Salad':'$19.75',
                    'Jumbo Spaghetti and Meatballs':'$20.45', 'Mushroom Swiss Burger':'$17.25',
                      'Clam Chowder Soup':'$9.25', 'Vegetarian Pizza':'$32.75', 'Buffalo Chicken Pizza':'$33.75'}
    
    result=random.choice(list(meal_choices.items()))

    meal_recommendation = {
       "meal recommendation": result[0],
       "price": result[1]
 }
    return json.dumps(meal_recommendation)
     
if __name__ == '__main__':
    port=os.environ.get('API_PORT', 5000)
    app.run(host="0.0.0.0", debug=True, port=port )



