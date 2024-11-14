from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")


def components(request):
    return render(request,"components.html")
