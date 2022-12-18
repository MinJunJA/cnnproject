from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from core.models import Nutrition

def index(request):
    return TemplateResponse(request, "snack.html")

def banana(request):
    object_nutrition = Nutrition.objects.get(name='바나나킥')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "banana.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def heim(request):
    object_nutrition = Nutrition.objects.get(name='화이트하임')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "heim.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def onion(request):
    object_nutrition = Nutrition.objects.get(name='양파링')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "onion.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def oreo(request):
    object_nutrition = Nutrition.objects.get(name='오레오')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "oreo.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def pepero(request):
    object_nutrition = Nutrition.objects.get(name='아몬드빼빼로')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "pepero.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def pie(request):
    object_nutrition = Nutrition.objects.get(name='후렌치파이')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "pie.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def pizza(request):
    object_nutrition = Nutrition.objects.get(name='벌집핏자')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "pizza.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def chip(request):
    object_nutrition = Nutrition.objects.get(name='포카칩')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "chip.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def shrimp(request):
    object_nutrition = Nutrition.objects.get(name='새우깡')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "shrimp.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })

def turtle(request):
    object_nutrition = Nutrition.objects.get(name='꼬북칩')
    total_content = object_nutrition.total_content
    calories = object_nutrition.calories
    carbohydrate = object_nutrition.carbohydrate
    protein = object_nutrition.protein
    fat = object_nutrition.fat
    return TemplateResponse(request, "turtle.html",{
        "total_content":total_content,
        "calories":calories,
        "carbohydrate":carbohydrate,
        "protein":protein,
        "fat":fat
    })