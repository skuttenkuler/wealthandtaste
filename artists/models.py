from django.db import models
import uuid

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    instagram_link = models.CharField(max_length=2000, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.first_name + " " + self.last_name     