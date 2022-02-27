from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)

class Location(models.Model):
    location = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=30)

class Image(models.Model):
    title = models.CharField(max_length =30)
    photographer = models.ForeignKey(Photographer)
    description = models.TextField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 
