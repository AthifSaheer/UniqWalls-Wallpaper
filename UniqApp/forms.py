from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomSignup(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


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