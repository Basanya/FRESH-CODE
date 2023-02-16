from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()


    def __str__(self):
        return self.title