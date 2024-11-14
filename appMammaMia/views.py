from django.shortcuts import render
from django.http import HttpResponse
from .models import Masa

def index(request):
    return render(request,"index.html")

def components(request):
    return render(request,"components.html")

def pizzas(request):
    return render(request,"pizzas.html", {'masas': Masa.objects.all()})