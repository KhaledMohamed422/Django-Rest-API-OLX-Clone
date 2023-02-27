from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid
# Create your models here.


class City (models.Model):
    
    name = models.CharField(max_length=20,blank=False,null=False,unique=True)
    
    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    
    city  = models.ForeignKey(City,  on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    
    def __str__(self):

        return self.user.username


class Images (models.Model):
    
    images = models.ImageField(upload_to='Images/Product/')    
    def __str__(self):
        return str(self.images)

class Advertisement(models.Model):
    
    CHOICES = [
    ('Mobiles', (
            ('Mobile_Phones', 'Mobile Phones'),
            ('Tablets', 'Tablets'),
            ('Accessories', 'Accessories'),
            ('otherwise', 'otherwise'),
        )
    ),
    ('Electronics&Appliances', (
            ('Computers&Accessories', 'Computers & Accessories'),
            ('Tv-Video-Audio', 'Tv - Video - Audio'),
            ('Games&Entertainment', 'Games & Entertainment'),
            ('Cameras&Accessories', 'Cameras & Accessories'),
            ('Fridge_AC_Washing_Machine', 'Fridge - AC - Washing Machine'),
            ('Kitchen&OtherAppliances', 'Kitchen & Other Appliances'),
        )
    ),
    ('Cars', (
            ('Spare_Parts', 'Spare Parts'),
            ('Other_Vehicles', 'Other Vehicles'),
            ('Spare_Parts', 'Spare Parts'),
            ('Cameras&Accessories', 'Cameras & Accessories'),
            ('Fridge_AC_Washing_Machine', 'Fridge - AC - Washing Machine'),
            ('Kitchen&OtherAppliances', 'Kitchen & Other Appliances'),
        )
    ),
    ('Bikes', (
            ('Bicycles', 'Bicycles'),
            ('Scooters', 'Scooters'),
            ('Spare_Parts', 'Spare Parts'),
            ('Motorcycles', 'Motorcycles'),
        )
    ),
   ]
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(Buyer,  on_delete=models.CASCADE)
    title = models.CharField(max_length=20 , null=False , blank= False)
    views = models.IntegerField(default=0,null=True , blank=True)
    price = models.FloatField(default=0.0,null=True , blank=True)
    states= models.IntegerField(default=0,null=True , blank=True)
    company = models.CharField(max_length=20 , null=False , blank= False)
    state = models.BooleanField(default=False)
    description = models.TextField(max_length=100,null=True , blank=True)
    images = models.ManyToManyField(Images)
    categories = models.CharField(max_length=30, choices=CHOICES, null=False, blank=False)
    is_trend = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
    

@receiver(pre_delete, sender=Advertisement)
def delete_advertisement_images(sender, instance, **kwargs):
    for image in instance.images.all():
        image.delete()
