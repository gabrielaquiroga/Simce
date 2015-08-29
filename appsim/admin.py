from django.contrib import admin
from .models import Establecimiento, Localidad, PruebaCienciasNaturales, PruebaLectura, PruebaMatematicas


# Register your models here

class LocalidadInline(admin.TabularInline):
    model=Localidad
    extra=  0

class PruebaCienciasInline(admin.TabularInline):
    model=PruebaCienciasNaturales
    extra= 0

class PruebaLecturaInline(admin.TabularInline):
    model= PruebaLectura
    extra=0


class PruebaMatematicasInline(admin.TabularInline):
    model= PruebaMatematicas
    extra= 0


class EstablecimientoAdmin(admin.ModelAdmin):
    
    list_display= ('nombre','rbd')
    inlines=(LocalidadInline, PruebaCienciasInline,PruebaMatematicasInline,PruebaLecturaInline)
    search_fields= [ 'nombre', 'rbd']

admin.site.register(Establecimiento,  EstablecimientoAdmin)
