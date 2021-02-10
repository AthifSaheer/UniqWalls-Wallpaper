from django import forms
from .models import *

class PictureAddingForm(forms.ModelForm):
    category : forms.ChoiceField()
    
    class Meta:
        model = Image
        fields = ["title", "category", "image"]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Title",
            }),
        }

class CategoryAddingForm(forms.ModelForm):
    category : forms.ChoiceField()
    
    class Meta:
        model = Category
        fields = ["title"]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Title",
            }),
        }