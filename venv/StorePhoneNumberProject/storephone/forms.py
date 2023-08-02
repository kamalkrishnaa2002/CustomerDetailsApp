from django import forms
from .models import Store, Category  # Import Category from models.py

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'phone_number', 'category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
