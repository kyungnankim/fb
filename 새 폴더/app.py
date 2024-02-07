from flask import Flask, render_template, request, redirect, url_for, session



app = Flask(__name__)

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
 
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)