from django.contrib import admin
from .models import Masa, Pizza, Ingrediente, Reserva
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin


admin.site.site_header = "Administración de MammaMia"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al panel de administración de MammaMia"

# Register your models here.
admin.site.register(Masa)
admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Reserva)


# Personalización de la visualización de los usuarios en el panel de administración
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

# Modificamos el UserAdmin registrado para usar nuestra versión personalizada
admin.site.unregister(User)  # Desregistramos el modelo User
admin.site.register(User, CustomUserAdmin)  # Volvemos a registrarlo con la configuración personalizada

# Si deseas personalizar el modelo Group, puedes hacerlo de la misma manera:
admin.site.unregister(Group)  # Desregistramos el modelo Group
admin.site.register(Group)  # Lo volvemos a registrar (sin cambios, si no lo personalizas