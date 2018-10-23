from django.contrib import admin
from .models import Model1, Model2, Model3

# Register your models here.

admin.site.register([Model1, Model2, Model3])