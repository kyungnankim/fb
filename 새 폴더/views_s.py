# myapp/views.py
from django.shortcuts import render
from .models import Image
from django.http import JsonResponse
from transformers import Diffusion
from PIL import Image as PILImage
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np
import os
'''
필요시
pip install transformers 설치  requirements 에 넣어두지 않았음
'''
def ai_processing_view(request):
    
    return render(request, 'myapp/ai_processing.html')

def predict_image(request):
    # Stable-diffusion 모델 로드
    model = Diffusion.from_pretrained('wd15-beta1-fp16.safetensors')

    # 요청에서 이미지 가져오기
    image_file = request.FILES.get('image')
    
    # 이미지를 임시 위치에 저장
    temp_image_path = 'temp_image.jpg'
    with open(temp_image_path, 'wb') as temp_image:
        for chunk in image_file.chunks():
            temp_image.write(chunk)

    # 이미지 전처리 코드
    img = image.load_img(temp_image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # 예측 수행
    predictions = model.predict(img_array)

    # 예측 결과 디코딩
    decoded_predictions = decode_predictions(predictions)

    # 예측된 클래스 가져오기
    predicted_class = decoded_predictions[0][0][1]

    # 예측된 이미지의 URL 가져오기
    image_url = '/media/temp_image.jpg'

    # 임시 이미지 파일 삭제
    os.remove(temp_image_path)

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