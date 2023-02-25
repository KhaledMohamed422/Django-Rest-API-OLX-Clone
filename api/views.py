from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Advertisement
from .Serializers import Home_AdvertisementSerializers

@api_view(['get'])
def Home(request):

    '''
    Home page just to show all categories
    Method --> Get
    Endpoint --> /home/
    Response 1 --> {"Name of categories": "URL for this category "}
    Response 2 --> {"Name of Product": "URL for this product " , "image" ": "" , "price ": ""} is te

    '''
    instance = Advertisement.objects.all()
    data = {}
    if instance:
        serializer = Home_AdvertisementSerializers(instance, context={'request': request}, many=True)
        data = serializer.data
#     is_ternd_instance =  instance.filter(is_trend=True)
#    if is_ternd_instance:
#          serializer = Home_is_trend_AdvertisementSerializers(instance)
#          data += serializer.data
    return Response(data)
