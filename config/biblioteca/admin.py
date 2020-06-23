from django.contrib import admin
from .models import *

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'editorial']
    list_display_links = ('titulo', 'editorial')

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1
    fields = ['titulo', 'editorial', 'paginas']

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']
    list_display_links = ('nombre', 'codigo')
    search_fields = ['nombre',]
    inlines = [LibroInline]

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'localizacion', 'libro']
    list_display_links = ('codigo', 'localizacion', 'libro')
    search_fields = ['libro__titulo']


class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['codigo', 'nombre', 'telefono']
    list_display_links = ('codigo', 'nombre',)

    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono')
        }),
    )
# Register your models here.

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UsuarioAdmin)
