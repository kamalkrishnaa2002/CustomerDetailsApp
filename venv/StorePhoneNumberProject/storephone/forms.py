from django import forms
from .models import Store, Category  # Import Category from models.py

# class StoreForm(forms.ModelForm):
#     class Meta:
#         model = Store
#         fields = ('name', 'phone_number', 'category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'phone_number', 'category']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # Remove all non-numeric characters
        phone_number = ''.join(filter(str.isdigit, phone_number))

        # Check if the phone number is greater than 10 digits
        if len(phone_number) > 10:
            # Check if the phone number starts with +91, 91, or 0
            if not (phone_number.startswith('+91') or phone_number.startswith('91') or phone_number.startswith('0')):
                raise forms.ValidationError("Invalid phone number format. It should start with +91, 91, or 0 if it's longer than 10 digits.")
        
        return phone_number

class ButtonClickedForm(forms.Form):
    store_id = forms.IntegerField(widget=forms.HiddenInput)