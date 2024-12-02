from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Masa, Pizza, Ingrediente, Reserva

def index(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    pizzas_por_masa = {}

    for masa in masas:
        pizza_barata = masa.pizza_set.order_by('precio').first()
        if pizza_barata:
            pizzas_por_masa[masa] = pizza_barata

    return render(request,"index.html", {'masas': masas, 'ingredientes':ingredientes, 'pizzas_por_masa':pizzas_por_masa})

#ESTE HAY QUE BORRARLO - COMPONENTS SON LAS PLANTILLAS A SECAS
def components(request):
    return render(request,"components.html")

def pizzas(request, masa_tipo):
    masa = get_object_or_404(Masa, nombre__iexact=masa_tipo)
    pizzas = masa.pizza_set.all()
    return render(request,"pizzas.html", {'pizzas': pizzas, 'masa': masa})

def pizza_desc(request, p_nombre):
    pizza = get_object_or_404(Pizza, nombre__iexact=p_nombre)
    return render(request, "descripcion_de_pizza.html", {'pizza':pizza})

def ingrediente_desc(request, i_nombre):
    ingrediente = get_object_or_404(Ingrediente, nombre__iexact=i_nombre)
    pizzas = Pizza.objects.filter(ingredientes__nombre__iexact=i_nombre)
    return render(request, "ingrediente.html", {'ingrediente': ingrediente, 'pizzas':pizzas})




def reservar_mesa(request):
    if request.method == 'POST':
        npersonas = request.POST.get('booktable-guests')
        hora = request.POST.get('booktable-time')
        fecha = request.POST.get('booktable-date')
        email = request.POST.get('booktable-email')

        if npersonas and hora and fecha and email:
            reserva = Reserva(
                npersonas = int(npersonas),
                hora = hora,
                fecha = fecha,
                email = email
            )
            reserva.save()
            return redirect('reserva_success', reserva_id=reserva.id)  #página de éxito
    return redirect('index')#de vuelta al loby literal

def reserva_success(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id) 
    return render(request, "reserva_success.html", {'reserva': reserva})