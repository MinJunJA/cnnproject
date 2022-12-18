from django.urls import path
from . import views

app_name = 'snack'

urlpatterns = [
    path('', views.index, name='index'),
    path('banana/', views.banana, name='banana'),
    path('heim/', views.heim, name='heim'),
    path('onion/', views.onion, name='onion'),
    path('oreo/', views.oreo, name='oreo'),
    path('pepero/', views.pepero, name='pepero'),
    path('pie/', views.pie, name='pie'),
    path('pizza/', views.pizza, name='pizza'),
    path('chip/', views.chip, name='chip'),
    path('shrimp/', views.shrimp, name='shrimp'),
    path('turtle/', views.turtle, name='turtle'),
]