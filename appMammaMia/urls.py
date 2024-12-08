from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('index.html', views.index, name='index'),
 path('components.html', views.components, name='Components'),
 path('pizzas/<str:masa_tipo>/', views.pizzas, name='pizzas' ),
 path('ingrediente/<str:i_nombre>/', views.ingrediente_desc, name='ingrediente_desc'),
 path('descripcion_de_pizza/<str:p_nombre>/', views.pizza_desc, name='pizza_desc'),
 path('reservar_mesa/', views.reservar_mesa, name='reservar_mesa'),
 path('reserva_success/<int:reserva_id>/', views.reserva_success, name='reserva_success'),
 path('pizzas_por_masa/<int:masa_id>/', views.pizzas_por_masa, name='pizzas_por_masa'),
]