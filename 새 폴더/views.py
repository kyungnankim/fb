# myapp/views.py
from django.shortcuts import render
from .models import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from django.http import JsonResponse
import numpy as np
import os

def predict_image(request):
    # 모델 로드
    model = load_model('modelB0.h5')

    # 데이터베이스에 저장된 이미지 불러오기
    image_instance = Image.objects.first()
    image_path = image_instance.image.path

    # 이미지 전처리를 위한 코드
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # 예측 수행
    predictions = model.predict(img_array)

    # 추후 예측 결과 디코딩
    decoded_predictions = decode_predictions(predictions)

    # 예측된 클래스
    predicted_class = decoded_predictions[0][0][1]

    # 예측된 이미지의 URL
    image_url = '/media/' + os.path.basename(image_path)

    # 응답 딕셔너리
    prediction_result = {
        'class': predicted_class,
        'image_url': image_url
    }

    # JSON 응답 반환
    return JsonResponse(prediction_result)

def home(request):
    products = [
        {"title": "Logo", "image_url": "/static/images/beyondLogo.jpg"},
        {"title": "Product 1", "image_url": "/static/images/3.png"},
        {"title": "Product 2", "image_url": "/static/images/2.png"},
        {"title": "Product 3", "image_url": "/static/images/1.png"},
    ]

    return render(request, 'myapp/home.html', {'products': products})
def ai_processing_view(request):
    return render(request, 'myapp/ai_processing.html')
'''
def predict_image(request):
    # Placeholder for your actual prediction logic using the h5 model
    # You need to replace this with your model prediction code
    # The response should be a dictionary containing the predicted class and image URL
    prediction_result = {
        'class': 'Cat',  # Replace with your predicted class
        'image_url': '/static/images/predicted_image.jpg'  # Replace with your predicted image URL
    }

    return JsonResponse(prediction_result)

'''    
#def home(request):
#    products = Product.objects.all()
#    return render(request, 'myapp/home.html', {'products': products})
