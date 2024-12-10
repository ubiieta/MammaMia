from django.contrib import admin
from .models import Masa, Pizza, Ingrediente, Reserva
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin


admin.site.site_header = "Administración de MammaMia"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al panel de administración de MammaMia"

admin.site.register(Masa)
admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Reserva)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

admin.site.unregister(User)  
admin.site.register(User, CustomUserAdmin)  

admin.site.unregister(Group) 
admin.site.register(Group)  