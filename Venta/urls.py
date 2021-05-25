
from django.contrib import admin
from django.urls import path
from Modulos.miregistro.views import Plantillauno, Plantillados

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Plantilla/', Plantillauno, name='Vista1'),
    path('Plantillas/', Plantillados, name='Vista2')
]