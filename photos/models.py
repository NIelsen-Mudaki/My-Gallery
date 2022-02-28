from django.db import models
import datetime as dt


# Create your models here.
class Photographer(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()
    def delete_photographer(self):
        self.delete()   
    @classmethod
    def display_photographer(cls):
        photographers= Photographer.objects.all()
        for photographer in photographers:
            return photographer

class Location(models.Model):
    location = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=30)

class Image(models.Model):
    title = models.CharField(max_length =30)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE,)
    description = models.TextField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

