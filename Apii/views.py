from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
# Create your views here.

class Home(ListView):
    model = Product
    template_name = "Apii/home.html"

