# from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
# import datetime as dt
# from .models import Article


# Create your views here.
def home(request):
    return render(request, 'index.html')
