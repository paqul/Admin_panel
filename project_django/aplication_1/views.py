from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Model1, Model2, Model3

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'main.html'

class Model1View(ListView):
    model = Model1

class Model2View(ListView):
    model = Model2

class Model1ViewCreate(CreateView):
    model = Model1
    fields = ['var1', 'var2', 'var3']

class Model1ViewUpdate(UpdateView):
    model = Model1
    fields = ['var1', 'var2', 'var3']

class Model1ViewDelete(DeleteView):
    model = Model1
    fields = ['var1', 'var2', 'var3']

class Model2ViewCreate(CreateView):
    model = Model2
    fields = ['whole_var']


