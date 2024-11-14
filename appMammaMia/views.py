from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Masa, Pizza

def index(request):
    return render(request,"index.html", {'masas': Masa.objects.all()})

def components(request):
    return render(request,"components.html")

def pizzas(request, masa_tipo):
    masa = get_object_or_404(Masa, nombre__iexact=masa_tipo)
    pizzas = Pizza.objects.filter(masa=masa)
    return render(request,"pizzas.html", {'pizzas': pizzas, 'masa': masa})