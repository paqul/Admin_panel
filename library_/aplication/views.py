from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from .models import Model1, Model2, Model3
from library_.aplication.models import Model1, Model2, Model3

# Create your views here.

class Model1View(ListView):
    model = Model1

class Model2ViewCreate(CreateView):
    model = Model2

class Model2ViewUpdate(UpdateView):
    model = Model2

class Model3ViewDelate(DeleteView):
    model = Model2

