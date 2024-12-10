from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Masa, Pizza, Ingrediente, Reserva
from django.http import HttpResponse
from .models import Masa, Pizza, Ingrediente, Reserva, Reserva
from .forms import ReservaForm

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
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Masa

def pizzas_por_masa(request, masa_id):
    masa = get_object_or_404(Masa, id=masa_id)
    pizzas = masa.pizza_set.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'pizzas': [
                {
                    'id': pizza.id,
                    'nombre': pizza.nombre,
                    'descripcion': pizza.descripcion,
                    'precio': pizza.precio,
                    'imagen': pizza.imagen.url if pizza.imagen else None  # Obtén la URL completa
                }
                for pizza in pizzas
            ]
        }
        return JsonResponse(data)

    return JsonResponse({'error': 'No es una solicitud AJAX'}, status=400)


# def reservar_mesa(request):
#     if request.method == 'POST':
#         npersonas = request.POST.get('booktable-guests')
#         hora = request.POST.get('booktable-time')
#         fecha = request.POST.get('booktable-date')
#         email = request.POST.get('booktable-email')

#         if npersonas and hora and fecha and email:
#             reserva = Reserva(
#                 npersonas = int(npersonas),
#                 hora = hora,
#                 fecha = fecha,
#                 email = email
#             )
#             reserva.save()
#             return redirect('reserva_success', reserva_id=reserva.id)  #página de éxito
#     return redirect('index')#de vuelta al loby literal




def reservar_mesa(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva_success', reserva_id=reserva.id)
    else:
        form = ReservaForm() 
    
    return render(request, 'index.html', {'form': form})  

def reserva_success(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id) 
    return render(request, "reserva_success.html", {'reserva': reserva})