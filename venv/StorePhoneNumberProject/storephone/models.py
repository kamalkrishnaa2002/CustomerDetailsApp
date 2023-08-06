from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    button_clicked = models.BooleanField(default=False)  # New field
    registered_date = models.DateTimeField(auto_now_add=True)  # New field
    clicked_at_date = models.DateTimeField(null=True, blank=True)  # New field

    def __str__(self):
        return self.name
