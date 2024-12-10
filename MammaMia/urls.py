"""
URL configuration for MammaMia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    Estoy cambiando esto para ver como se hace un push jajaj
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import set_language
from appMammaMia  import views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Para soporte de idiomas
    path('i18n/setlang/', set_language, name='set_language'),
    path('test-language/', views.test_language, name='test_language'),
    path('', include('appMammaMia.urls')),  # Cargar las URLs de tu app

     
]

# Usar i18n_patterns para manejar el idioma por defecto y las rutas de administración
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),  
    prefix_default_language=False,  # No se agregará el idioma por defecto a la URL
)