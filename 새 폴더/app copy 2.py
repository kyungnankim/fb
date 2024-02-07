from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    # 가상의 데이터
    photos = [
        {"url": "/static/images/2.png", "caption":  "/static/images/2.png"},
        {"url":  "/static/images/2.png", "caption":  "/static/images/2.png"},
        {"url": "/static/images/2.png", "caption":  "/static/images/2.png"},
        {"url":  "/static/images/2.png", "caption":  "/static/images/2.png"},
        {"url": "/static/images/2.png", "caption":  "/static/images/2.png"},
        {"url":  "/static/images/2.png", "caption":  "/static/images/2.png"},
    ]

    user_info = {"username": "my-style", "followers": 1000, "following": 500}

    for i, photo in enumerate(photos):
        photo['id'] = i

    return render_template('index.html', photos=photos, user_info=user_info)
if __name__ == '__main__':
    app.run(debug=True)
