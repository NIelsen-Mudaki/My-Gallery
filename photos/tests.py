from django.test import TestCase
from .models import Photographer,Location,Category, Image

# Create your tests here.
class PhotographerTest(TestCase):
    def setUp(self):
        self.nielsen= Photographer(name = 'Nielsen',email='jumbanielsen@gmail.com', phone_number ='0717899262')

    def test_instance(self):
        self.assertTrue(isinstance(self.nielsen,Photographer))

    #testing save method
    def test_save(self):
        self.nielsen.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)

    #testing delete method
    def test_delete(self):
        self.nielsen.save_photographer()
        self.nielsen.delete_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) == 0)

    #testing displaying model
    def test_display(self):
        self.nielsen.save_photographer()
        self.nielsen.display_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)