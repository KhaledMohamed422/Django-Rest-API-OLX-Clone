from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *


app_name = 'api'
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('ads', AdViewSet, basename='ads')

urlpatterns = [
    # path('home/',views.Home,name='Home' ),
    # path('Items/<slug:subcategory>/',views.Category_Advertisements,name='Category_Advertisements'),
    # path('Items/<uuid:Id>/',views.blank,name='blank'),
    path('', include(router.urls)),

]