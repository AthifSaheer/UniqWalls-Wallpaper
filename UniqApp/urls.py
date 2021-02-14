from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category', CategoryView.as_view(), name="category"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),

    path('adminpage', AdminPageView.as_view(), name="adminpage"),

    path('image-upload-view', ImageUploadView.as_view(), name="imageuploadview"),
    path('image-delete-view', ImageDeleteView.as_view(), name="imagedeleteview"),
    path('image-delete-button/<int:pk>/', ImageDeleteButton.as_view(), name="imagedeletebutton"),

    path('category-adding-view', CategoryAddingView.as_view(), name="categoryaddingview"),
    path('category-delete-view', CategoryDeleteView.as_view(), name="categorydeleteview"),
    path('category-delete-button/<int:pk>/', CategoryDeleteButton.as_view(), name="categorydeletebutton"),
    
    # Authentication -------------------------------
    path('signin', SigninView.as_view(), name="signin"),
    path('signup', SignupView.as_view(), name="signup"),
    path('logout', LogoutView.as_view(), name="logout"),
]
