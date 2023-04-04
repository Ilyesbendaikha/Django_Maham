from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class client(models.Model):
    name = models.CharField(max_length=50,null=True)
    phonenumber = models.CharField(max_length=50,null=True)
    passportnumber = models.CharField(max_length=50,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    statue = [
        ('Available','Available'),
        ('Not Available','Not Available'),
    ]
    name_country = models.CharField(max_length=50,null=True)
    price_place = models.FloatField()
    place_image = models.ImageField(null=True)
    statue = models.CharField(choices=statue, max_length=50)

    def __str__(self):
        return self.name_country
    


class voyage(models.Model):
    Category = [
        ('2 beds','2 beds'),
        ('3 beds','3 beds'),
        ('4 beds','4 beds'),
    ]
    room = models.CharField(choices=Category, max_length=50,null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.room
    



class order(models.Model):
    client = models.ForeignKey(client, null=True, on_delete=models.CASCADE)
    voyage = models.ForeignKey(voyage, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    

    def __str__(self):
        return self.client.name
    
    def add(self):
        x = self.place.price_place + self.voyage.price
        return x

    

