from django.contrib import admin
from .models import Masa, Pizza, Ingrediente, Reserva

# Register your models here.
admin.site.register(Masa)
admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Reserva)