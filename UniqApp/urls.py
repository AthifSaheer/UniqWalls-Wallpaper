from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category', CategoryView.as_view(), name="category"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),
    path('adminpage', AdminPageView.as_view(), name="adminpage"),
    path('image-upload-view', ImageUploadView.as_view(), name="imageuploadview"),
    path('category-adding-view', CategoryAddingView.as_view(), name="categoryaddingview"),
]
