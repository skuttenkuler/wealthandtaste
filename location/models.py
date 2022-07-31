from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100,default="Nashville")
    state = models.CharField(max_length=2,default="TN")
    zipcode = models.CharField(max_length=5, null=True)


    def __str__(self):
        return self.title