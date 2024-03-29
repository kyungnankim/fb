from flask import Flask, render_template, request, jsonify
#from flask_ngrok import run_with_ngrok  # Import run_with_ngrok

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def home():
    products = [
        {"title": "Logo", "image_url": "/static/images/beyondLogo.jpg"},
        {"title": "Product 1", "image_url": "/static/images/3.png"},
        {"title": "Product 2", "image_url": "/static/images/2.png"},
        {"title": "Product 3", "image_url": "/static/images/1.png"},
    ]
    return render_template('home.html', products=products)

@app.route('/ai_processing/')
def ai_processing():
    return render_template('ai_processing.html')

@app.route('/predict_image/', methods=['POST'])
def predict_image():
    prediction_result = {
        'class': 'Cat',
        'image_url': '/static/images/predicted_image.jpg' 
    }
    return jsonify(prediction_result)
if __name__ == '__main__':
    app.run()

'''
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    products = [
        {"title": "Logo", "image_url": "/static/images/beyondLogo.jpg"},
        {"title": "Product 1", "image_url": "/static/images/3.png"},
        {"title": "Product 2", "image_url": "/static/images/2.png"},
        {"title": "Product 3", "image_url": "/static/images/1.png"},
    ]
    return render_template('home.html', products=products)

@app.route('/ai_processing/')
def ai_processing():
    return render_template('ai_processing.html')

@app.route('/predict_image/', methods=['POST'])
def predict_image():
    # Placeholder for your actual prediction logic using the h5 model
    # You need to replace this with your model prediction code
    # The response should be a dictionary containing the predicted class and image URL
    prediction_result = {
        'class': 'Cat',  # Replace with your predicted class
        'image_url': '/static/images/predicted_image.jpg'  # Replace with your predicted image URL
    }
    return jsonify(prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
'''
