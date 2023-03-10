from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Advertisement
# from .Serializers import Home_AdvertisementSerializers , Home_is_trend_AdvertisementSerializers , Category_AdvertisementsSerializers
from rest_framework import viewsets
from .models import *
from .Serializers import *

# @api_view(['get'])
# def Home(request):

#     '''
#     Home page just to show all categories
#     Method --> Get
#     Endpoint --> /home/
#     Response 1 --> {"Name of categories": "URL for this category "}
#     Response 2 --> {"Name of Product": "URL for this product " , "image" ": "" , "price ": ""} is te

#     '''
#     instance = Advertisement.objects.all()
#     data = {}
#     if instance:
#         serializer = Home_AdvertisementSerializers(instance, context={'request': request}, many=True)
#         data = serializer.data
#     is_ternd_instance =  instance.filter(is_trend=True)
    
#     if is_ternd_instance:
#          serializer = Home_is_trend_AdvertisementSerializers(is_ternd_instance, context={'request': request}, many=True)
#          data.append(serializer.data)
#     return Response(data)


# @api_view(['get'])
# def Category_Advertisements(request,subcategory):
    
#     '''
#     This view should to show all Advertisements for
#     any Category at the slug 
#     '''
    
#     instance = Advertisement.objects.filter(categories=subcategory)
#     if instance:
#         serializer = Category_AdvertisementsSerializers(instance, many=True,context={'request': request})
#         data = serializer.data
#     return Response(data)


# @api_view(['get'])
# def blank(request):
#     return Response({})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    
    

class AdViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'id' # to get object by id 