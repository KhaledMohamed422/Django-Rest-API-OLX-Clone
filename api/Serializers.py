from rest_framework import serializers
from django.urls import reverse
from .models import Advertisement

class Home_AdvertisementSerializers(serializers.ModelSerializer):


    urls = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ['categories', 'urls']

    def get_urls(self, obj):
        '''
        This method returns the serialized URLs for each subcategory.
        The obj parameter refers to the instance of the Advertisement model being serialized.
        The urls dictionary will contain the URLs for each subcategory.
        The CHOICES attribute of the Advertisement model contains the possible choices for the categories field.
        The for loop iterates over each choice and checks if it matches the categories value of the current instance.
        If there is a match, the URL for the subcategory is constructed using the reverse function with the api:subcategory view name and the subcategory argument.
        Finally, the build_absolute_uri method is called on the request object in the serializer's context to convert the relative URL to an absolute URL. This is necessary because the URLs will be included in the serialized JSON response, and clients need to be able to access them.
        The serialized URLs are returned as a dictionary with the subcategories as keys.
        '''
        urls = {}
        for category, subcategories in obj.CHOICES:
            for subcategory, label in subcategories:
                if obj.categories == subcategory:
                    url_name = 'api:Category_Advertisements'
                    url = reverse(url_name, args=[subcategory])
                    urls[subcategory] = self.context['request'].build_absolute_uri(url)
        return urls
        '''
        urls[subcategory] is assigning a value to the subcategory key in the urls dictionary.
        self.context is a dictionary containing the context data for the current serializer. It contains information like the current request and view.
        self.context['request'] accesses the current HTTP request object.
        build_absolute_uri is a method of the current request object, which returns the complete URL for the given URL. It takes a relative URL (like /Items/Tablets/) and converts it to an absolute URL (like http://127.0.0.1:8000/Items/Tablets/).
        So, urls[subcategory] = self.context['request'].build_absolute_uri(url) is assigning the absolute URL to the subcategory key in the urls dictionary, so that it can be used in the serialized response.
         '''

class Home_is_trend_AdvertisementSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:blank',
        lookup_field='Id'
    )
    class Meta:
        model = Advertisement
        fields = ['images', 'price', 'url']
 

class Category_AdvertisementsSerializers(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:blank',
        lookup_field='Id'
    )
   
    class Meta:
        model = Advertisement
        fields = ['title','company','images', 'price', 'description','url']


        
                
    
        
