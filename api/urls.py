from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'api'

urlpatterns = [
    path('home/',views.Home,name='Home' ),
    path('Items/<slug:subcategory>/',views.Home,name='subcategory'),

]