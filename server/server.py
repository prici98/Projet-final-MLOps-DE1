from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from prediction import text_to_vector
from prediction import fill_data
import pickle

app = Flask(__name__)
cors = CORS(app, resources={
    r"/api/*": {"origins": "http://localhost:3000"},
    r"/*": {"origins": "http://localhost:3000"}
})

@app.route('/', methods=['POST'])
def make_prediction():
    data = request.json
    title = text_to_vector(data['title'])
    genre = data['genre'].rsplit(',', 1)
    description = text_to_vector(data['description'])
    type = data['type'].rsplit(',', 1)
    producer = data['producer'].rsplit(',', 1)
    studio = data['studio'].rsplit(',', 1)
    
    df = pd.read_csv('data.csv')
    donnee_entrer= type + producer + studio + genre
    
    df= fill_data(donnee_entrer,description,title,df)
    df = df.drop(['Rating', 'Unnamed: 0'], axis=1)
    
    with open('model.pkl', 'rb') as f:
        models = pickle.load(f)

    y_pred = models.predict(df)
    
    return jsonify({'prediction': str(y_pred[0])})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)

