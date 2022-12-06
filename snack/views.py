from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from core.models import Snack,Nutrition # models.py 안의 Snack 클래스 호출



def index(request):

    # 바나나킥
    snack_banana = Snack.objects.get(name="바나나킥")
    nutrition_banana = Nutrition.objects.get(name="바나나킥")

    banana_name = snack_banana.name
    banana_info = snack_banana.info
    banana_price = str(snack_banana.price)
    banana_total_content = str(nutrition_banana.total_content)
    banana_protein = str(nutrition_banana.protein)
    banana_fat = str(nutrition_banana.fat)
    banana_carbohydrate = str(nutrition_banana.carbohydrate)

    # 포카칩
    snack_chip = Snack.objects.get(name="포카칩")
    nutrition_chip = Nutrition.objects.get(name="포카칩")

    chip_name = snack_chip.name
    chip_info = snack_chip.info
    chip_price = str(snack_chip.price)
    chip_total_content = str(nutrition_chip.total_content)
    chip_protein = str(nutrition_chip.protein)
    chip_fat = str(nutrition_chip.fat)
    chip_carbohydrate = str(nutrition_chip.carbohydrate)

    # 화이트하임
    snack_heim = Snack.objects.get(name="화이트하임")
    nutrition_heim = Nutrition.objects.get(name="화이트하임")

    heim_name = snack_heim.name
    heim_info = snack_heim.info
    heim_price = str(snack_heim.price)
    heim_total_content = str(nutrition_heim.total_content)
    heim_protein = str(nutrition_heim.protein)
    heim_fat = str(nutrition_heim.fat)
    heim_carbohydrate = str(nutrition_heim.carbohydrate)

    # 양파링
    snack_onion = Snack.objects.get(name="양파링")
    nutrition_onion = Nutrition.objects.get(name="양파링")

    onion_name = snack_onion.name
    onion_info = snack_onion.info
    onion_price = str(snack_onion.price)
    onion_total_content = str(nutrition_onion.total_content)
    onion_protein = str(nutrition_onion.protein)
    onion_fat = str(nutrition_onion.fat)
    onion_carbohydrate = str(nutrition_onion.carbohydrate)

    # 오레오
    snack_oreo = Snack.objects.get(name="오레오")
    nutrition_oreo = Nutrition.objects.get(name="오레오")

    oreo_name = snack_oreo.name
    oreo_info = snack_oreo.info
    oreo_price = str(snack_oreo.price)
    oreo_total_content = str(nutrition_oreo.total_content)
    oreo_protein = str(nutrition_oreo.protein)
    oreo_fat = str(nutrition_oreo.fat)
    oreo_carbohydrate = str(nutrition_oreo.carbohydrate)

    # 아몬드빼빼로
    snack_pepero = Snack.objects.get(name="아몬드빼빼로")
    nutrition_pepero = Nutrition.objects.get(name="아몬드빼빼로")

    pepero_name = snack_pepero.name
    pepero_info = snack_pepero.info
    pepero_price = str(snack_pepero.price)
    pepero_total_content = str(nutrition_pepero.total_content)
    pepero_protein = str(nutrition_pepero.protein)
    pepero_fat = str(nutrition_pepero.fat)
    pepero_carbohydrate = str(nutrition_pepero.carbohydrate)

    # 후렌치파이
    snack_pie = Snack.objects.get(name="후렌치파이")
    nutrition_pie = Nutrition.objects.get(name="후렌치파이")

    pie_name = snack_pie.name
    pie_info = snack_pie.info
    pie_price = str(snack_pie.price)
    pie_total_content = str(nutrition_pie.total_content)
    pie_protein = str(nutrition_pie.protein)
    pie_fat = str(nutrition_pie.fat)
    pie_carbohydrate = str(nutrition_pie.carbohydrate)

    # 벌집핏자
    snack_pizza = Snack.objects.get(name="벌집핏자")
    nutrition_pizza = Nutrition.objects.get(name="벌집핏자")

    pizza_name = snack_pizza.name
    pizza_info = snack_pizza.info
    pizza_price = str(snack_pizza.price)
    pizza_total_content = str(nutrition_pizza.total_content)
    pizza_protein = str(nutrition_pizza.protein)
    pizza_fat = str(nutrition_pizza.fat)
    pizza_carbohydrate = str(nutrition_pizza.carbohydrate)

    # 새우깡
    snack_shrimp = Snack.objects.get(name="새우깡")
    nutrition_shrimp = Nutrition.objects.get(name="새우깡")

    shrimp_name = snack_shrimp.name
    shrimp_info = snack_shrimp.info
    shrimp_price = str(snack_shrimp.price)
    shrimp_total_content = str(nutrition_shrimp.total_content)
    shrimp_protein = str(nutrition_shrimp.protein)
    shrimp_fat = str(nutrition_shrimp.fat)
    shrimp_carbohydrate = str(nutrition_shrimp.carbohydrate)

    # 꼬북칩
    snack_turtle = Snack.objects.get(name="꼬북칩")
    nutrition_turtle = Nutrition.objects.get(name="꼬북칩")

    turtle_name = snack_turtle.name
    turtle_info = snack_turtle.info
    turtle_price = str(snack_turtle.price)
    turtle_total_content = str(nutrition_turtle.total_content)
    turtle_protein = str(nutrition_turtle.protein)
    turtle_fat = str(nutrition_turtle.fat)
    turtle_carbohydrate = str(nutrition_turtle.carbohydrate)                    

    return TemplateResponse(request,
    "snack.html", # 데이터 가져올 때 이 부분만 바꿔서 복붙하시면 mysql의 데이터를 가져오실 수 있습니다. 
    {
        "banana_name":banana_name,
        "banana_info":banana_info,
        "banana_price":banana_price,
        "banana_total_content":banana_total_content,
        "banana_protein":banana_protein,
        "banana_fat":banana_fat,
        "banana_carbohydrate":banana_carbohydrate,

        "chip_name":chip_name,
        "chip_info":chip_info,
        "chip_price":chip_price,
        "chip_total_content":chip_total_content,
        "chip_protein":chip_protein,
        "chip_fat":chip_fat,
        "chip_carbohydrate":chip_carbohydrate,

        "heim_name":heim_name,
        "heim_info":heim_info,
        "heim_price":heim_price,
        "heim_total_content":heim_total_content,
        "heim_protein":heim_protein,
        "heim_fat":heim_fat,
        "heim_carbohydrate":heim_carbohydrate,

        "onion_name":onion_name,
        "onion_info":onion_info,
        "onion_price":onion_price,
        "onion_total_content":onion_total_content,
        "onion_protein":onion_protein,
        "onion_fat":onion_fat,
        "onion_carbohydrate":onion_carbohydrate,

        "oreo_name":oreo_name,
        "oreo_info":oreo_info,
        "oreo_price":oreo_price,
        "oreo_total_content":oreo_total_content,
        "oreo_protein":oreo_protein,
        "oreo_fat":oreo_fat,
        "oreo_carbohydrate":oreo_carbohydrate,

        "pepero_name":pepero_name,
        "pepero_info":pepero_info,
        "pepero_price":pepero_price,
        "pepero_total_content":pepero_total_content,
        "pepero_protein":pepero_protein,
        "pepero_fat":pepero_fat,
        "pepero_carbohydrate":pepero_carbohydrate,

        "pie_name":pie_name,
        "pie_info":pie_info,
        "pie_price":pie_price,
        "pie_total_content":pie_total_content,
        "pie_protein":pie_protein,
        "pie_fat":pie_fat,
        "pie_carbohydrate":pie_carbohydrate,

        "pizza_name":pizza_name,
        "pizza_info":pizza_info,
        "pizza_price":pizza_price,
        "pizza_total_content":pizza_total_content,
        "pizza_protein":pizza_protein,
        "pizza_fat":pizza_fat,
        "pizza_carbohydrate":pizza_carbohydrate,

        "shrimp_name":shrimp_name,
        "shrimp_info":shrimp_info,
        "shrimp_price":shrimp_price,
        "shrimp_total_content":shrimp_total_content,
        "shrimp_protein":shrimp_protein,
        "shrimp_fat":shrimp_fat,
        "shrimp_carbohydrate":shrimp_carbohydrate,

        "turtle_name":turtle_name,
        "turtle_info":turtle_info,
        "turtle_price":turtle_price,
        "turtle_total_content":turtle_total_content,
        "turtle_protein":turtle_protein,
        "turtle_fat":turtle_fat,
        "turtle_carbohydrate":turtle_carbohydrate                                        
    }
    )
