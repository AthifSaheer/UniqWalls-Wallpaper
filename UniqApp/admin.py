from django.contrib import admin
from .models import Image, Category

admin.site.register([Image, Category])