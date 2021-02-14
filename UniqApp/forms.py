from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OwnUserRegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class OwnUserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = User
    #     fields = ('username', 'password')

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