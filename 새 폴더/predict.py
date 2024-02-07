from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# 모델 경로
model_path = 'models/Stable-diffusion'
model = tf.saved_model.load(model_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict-image/', methods=['POST'])
def predict_image():
    try:
        image_file = request.files['image']
        image = Image.open(image_file.stream).convert('RGB')
        image = image.resize((224, 224)) 

        image_array = np.array(image) 
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model(image_array)['predictions'][0].numpy()

        result = {
            'class': str(np.argmax(prediction)),
            'image_url': '/static/images/4.png', 
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
