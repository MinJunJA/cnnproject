import os
import numpy as np
from .models import Snack,Nutrition # models.py 안의 Snack 클래스 호출

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
# https://im-nanna.tistory.com/27 //MultiValueDictKeyError에 대한 설명
# https://windybay.net/post/39/

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.db import connection



class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def index(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        
        # Read the image

        imag = load_img(path,target_size = (75,75))
        imag = img_to_array(imag)
        img = imag.reshape(1,75,75,3)
        img = img.astype('float32')
        test_image = img/255.0

        # load model(CNN)
        model = tf.keras.models.load_model(os.getcwd() + '/3rd_vgg16_2.h5')
        result = model.predict(test_image)

        # ----------------
        # LABELS
        # Banana 0
        # Chip 1
        # Heim 2
        # Onion 3
        # Oreo 4
        # Pepero 5
        # Pie 6
        # Pizza 7
        # Shrimp 8
        # Turtle 9
        # ----------------
        print("Prediction: " + str(np.argmax(result)))

        prediction = np.argmax(result)
        accuracy = str(int(np.max(result)*100))+"%"
        snack_object = Snack.objects.get(id=prediction+1)
        nutrition_object = Nutrition.objects.get(id=prediction+1)

        name = snack_object.name
        info = snack_object.info
        price = snack_object.price

        total_content = str(nutrition_object.total_content) # total_content: 총 용량
        calories = str(nutrition_object.calories)

        if name=="바나나킥":
            eng_name="banana"
        elif name=="포카칩":
            eng_name="chip"
        elif name=="화이트하임":
            eng_name="heim"
        elif name=="양파링":
            eng_name="onion"
        elif name=="오레오":
            eng_name="oreo"
        elif name=="아몬드빼빼로":
            eng_name="pepero"
        elif name=="후렌치파이":
            eng_name="pie"
        elif name=="벌집핏자":
            eng_name="pizza"
        elif name=="새우깡":
            eng_name="shrimp"
        elif name=="꼬북칩":
            eng_name="turtle"
        else:
            eng_name="#"

        return TemplateResponse(
            request,
            "pred.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
                "name": name,
                "eng_name": eng_name,
                "accuracy": accuracy,
                "info": info,
                "price": price,
                "total_content": total_content,
                "calories": calories
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": "업로드한 이미지가 없습니다."
            },
        )


def pred(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        
        # Read the image

        imag = load_img(path,target_size = (75,75))
        imag = img_to_array(imag)
        img = imag.reshape(1,75,75,3)
        img = img.astype('float32')
        test_image = img/255.0

        # load model(CNN)
        model = tf.keras.models.load_model(os.getcwd() + '/3rd_cnn_1.h5')
        result = model.predict(test_image)

        # ----------------
        # LABELS
        # Banana 0
        # Chip 1
        # Heim 2
        # Onion 3
        # Oreo 4
        # Pepero 5
        # Pie 6
        # Pizza 7
        # Shrimp 8
        # Turtle 9
        # ----------------
        print("Prediction: " + str(np.argmax(result)))

        prediction = np.argmax(result)
        snack_object = Snack.objects.get(id=prediction+1)
        nutrition_object = Nutrition.objects.get(id=prediction+1)

        name = snack_object.name
        info = snack_object.info
        price = snack_object.price

        total_content = str(nutrition_object.total_content)
        calories = str(nutrition_object.calories)

        return TemplateResponse(
            request,
            "pred.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
                "name": name,
                "info": info,
                "price": price,
                "total_content": total_content,
                "calories": calories
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": "업로드한 이미지가 없습니다."
            },
        )

def banana(request):
    return TemplateResponse(request,
    "banana.html",
    )

def pepero(request):
    return TemplateResponse(request,
    "pepero.html",
    )

def chip(request):
    return TemplateResponse(request,
    "chip.html",
    )

def heim(request):
    return TemplateResponse(request,
    "heim.html",
    )

def onion(request):
    return TemplateResponse(request,
    "onion.html",
    )

def oreo(request):
    return TemplateResponse(request,
    "oreo.html",
    )

def pie(request):
    return TemplateResponse(request,
    "pie.html",
    )

def pizza(request):
    return TemplateResponse(request,
    "pizza.html",
    )

def shrimp(request):
    return TemplateResponse(request,
    "shrimp.html",
    )

def turtle(request):
    return TemplateResponse(request,
    "turtle.html",
    )