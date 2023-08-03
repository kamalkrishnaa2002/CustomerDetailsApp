# Create your models here.
# storephone/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    button_clicked = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.name