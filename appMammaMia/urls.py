from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
 path('test-language/', views.test_language, name='test_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)