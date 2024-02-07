from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, firestore, storage
import pyrebase
import requests
import os
import random
from datetime import datetime
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'my-style'
app.config['UPLOAD_FOLDER'] = 'static/upload'  # 업로드 폴더 설정

cred = credentials.Certificate("my-style-5649d-firebase-adminsdk-kufso-1f9b9aecef.json")
firebase_admin.initialize_app(cred)
firebaseConfig = {
    "apiKey": "AIzaSyDK5WsV0Udf-Ajr_5RsdofOtpyWg1sn1U0",
    "authDomain": "my-style-5649d.firebaseapp.com",
    "databaseURL": "https://my-style-5649d-default-rtdb.firebaseio.com",
    "projectId": "my-style-5649d",
    "storageBucket": "my-style-5649d.appspot.com",
    "messagingSenderId": "1049533452766",
    "appId": "1:1049533452766:web:3f0b5c00ac2d97e66d8d4f",
    "measurementId": "G-24Y5T3HCEP"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

categories = ["New In", "hood", "sweat shirts"]
products = [
    {"id": 1, "name": "User 1", "category": "hood", "image": "/static/images/2024SS_hood_product_S1023193891_St70_G7.5.jpeg", "likes": 0},
    {"id": 2, "name": "User 2", "category": "hood", "image": "/static/images/2024SS_hood_product_S1023193892_St70_G7.5.jpeg", "likes": 0},
    {"id": 3, "name": "User 3", "category": "New In", "image": "/static/images/2024SS_hood_product_S1023193893_St70_G7.5.jpeg", "likes": 0},
    {"id": 4, "name": "User 4", "category": "hood", "image": "/static/images/2024SS_hood_product_S1023193894_St70_G7.5.jpeg", "likes": 0},
    {"id": 5, "name": "User 5", "category": "hood", "image": "/static/images/2024SS_hood_product_S4066034769_St70_G7.5.jpeg", "likes": 0},
    {"id": 6, "name": "User 6", "category": "New In",  "image": "/static/images/2024SS_hood_product_S4066034770_St70_G7.5.jpeg", "likes": 0},
    
    {"id": 7, "name": "User 7", "category": "hood", "image": "/static/images/2024SS_hood_product_S4066034771_St70_G7.5.jpeg", "likes": 0},
    {"id": 8, "name": "User 8", "category": "hood","image": "/static/images/2024SS_hood_product_S4066034772_St70_G7.5.jpeg", "likes": 0},
    {"id": 9, "name": "User 9", "category": "New In",  "image": "/static/images/2024SS_sweat_shirts_model_S1226204908_St70_G7.5.jpeg", "likes": 0},
    {"id": 10, "name": "User 10", "category": "sweat shirts", "image": "/static/images/2024SS_sweat_shirts_model_S1226204910_St70_G7.5.jpeg", "likes": 0},
    {"id": 11, "name": "User 11", "category": "New In", "image": "/static/images/2024SS_sweat_shirts_model_S1226204909_St70_G7.5.jpeg", "likes": 0},
    {"id": 12, "name": "User 12", "category": "sweat shirts","image": "/static/images/2024SS_sweat_shirts_model_S1226204911_St70_G7.5.jpeg", "likes": 0},

    {"id": 13, "name": "User 13", "category": "sweat shirts", "image": "/static/images/2024SS_sweat_shirts_product_S3892092705_St70_G7.5.jpeg", "likes": 0},
    {"id": 14, "name": "User 14", "category": "sweat shirts", "image": "/static/images/2024SS_sweat_shirts_S1066249975_St70_G7.5.jpeg", "likes": 0},
    {"id": 15, "name": "User 15", "category": "New In",  "image": "/static/images/2024SS_sweat_shirts_S1066249976_St70_G7.5.jpeg", "likes": 0},
    {"id": 16, "name": "User 16", "category": "sweat shirts", "image": "/static/images/2024SS_sweat_shirts_S1066249977_St70_G7.5.jpeg", "likes": 0},
    {"id": 17, "name": "User 17", "category": "New In", "image": "/static/images/2024SS_sweat_shirts_S1066249982_St70_G7.5.jpeg", "likes": 0},
    {"id": 18, "name": "User 18", "category": "New In", "image": "/static/images/2024SS_sweat_shirts_S1066249983_St70_G7.5.jpeg", "likes": 0},
]

@app.route('/')
def home():
    user_uid = session.get('user_uid')
    welcome_message = None

    if user_uid:
        user_data = db.child('users').child(user_uid).get().val()
        print("User Data:", user_data)

        if user_data:
            welcome_message = f"Welcome, {user_data.get('username', 'Guest')}!"

    return render_template('home.html', categories=categories, products=products, welcome_message=welcome_message)


@app.route('/category/<selected_category>')
def category(selected_category):
    filtered_products = [product for product in products if product['category'] == selected_category]
    return render_template('home.html', categories=categories, products=filtered_products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = auth.sign_in_with_email_and_password(email, password)

            session['user_uid'] = user['localId']

            return redirect(url_for('home'))

        except auth.AuthError as e:
            error_message = str(e)
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/ai')
def ai():
     return render_template('ai_processing.html')

@app.route('/predict_image/', methods=['POST'])
def predict_image():
    prediction_result = {
        'class': 'Cat',
        'image_url': '/static/images/predicted_image.jpg' 
    }
    return jsonify(prediction_result)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if len(password) < 6:
            error_message = "Password should be at least 6 characters"
            return render_template('signup.html', error_message=error_message),

        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_data = {
                'username': username,
                'email': email,
                'uid': user['localId']
            }

            db.child('users').child(user['localId']).set(user_data)
            session['user_uid'] = user['localId']
            return redirect(url_for('home'))

        except requests.exceptions.HTTPError as e:
            error_message = str(e)
            print("HTTPError:", str(e))
            return render_template('signup.html', error_message=error_message),
        except Exception as e:
            print("Firebase Error:", str(e))
            return render_template('signup.html', error_message="Registration failed. Please try again."),

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


from flask import render_template

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 클라이언트로부터 이미지 파일의 경로를 받음
        image_path = request.json['image_path']
        
        # 이미지 파일의 경로에서 이미지 파일명을 추출
        filename = os.path.basename(image_path)
        
        try:
            # 이미지 파일을 읽어와서 Firebase Storage에 업로드
            with open(image_path, 'rb') as file:
                storage.child('upload/' + filename).put(file)  # Corrected directory name to 'upload'
            
            # Firebase Storage에 업로드된 이미지의 URL을 얻어옴
            image_url = storage.child('upload/' + filename).get_url(None)  # Corrected directory name to 'upload'
            
            # Firebase Database에 이미지 정보 저장
            db.child('images').push({'filename': filename, 'url': image_url})
            
            return jsonify({'success': True}), 200
        except Exception as e:
            print('Error:', e)
            return jsonify({'success': False, 'error': str(e)}), 500
    
    # Choose a random image from static/img folder
    img_folder = os.path.join(app.root_path, 'static', 'img')
    img_files = os.listdir(img_folder)
    random_img = random.choice(img_files)
    random_img_path = os.path.join('static', 'img', random_img)

    return render_template('upload.html', random_img=random_img_path)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
