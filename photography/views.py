from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo
# Create your views here.

class PhotoList(ListView):
    model=Photo