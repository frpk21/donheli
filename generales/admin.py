from django.contrib import admin

from generales.models import Categoria, Portada, Reflexiones, Noticias

from django.contrib.admin.widgets import AutocompleteSelect

import random


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'imagen',)
    ordering = ('id', )

    class Meta:
        model = Categoria

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class PortadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen',)
    ordering = ('nombre', )

    class Meta:
        model = Portada

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class ReflexionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'url_video', )
    ordering = ('fecha', 'nombre', )

    class Meta:
        model = Reflexiones

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


"""
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nombre', 'imagen',)
    ordering = ('id', )

    class Meta:
        model = SubCategoria

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
"""

class NoticiasAdmin(admin.ModelAdmin):

    list_display = ('categoria', 'titulo', 'subtitulo', 'orden_destacado', 'imagen_destacado', 'modificado','activo', )
    fields = ['categoria', 'titulo', 'subtitulo', ('orden_destacado', 'imagen_destacado'), 'descripcion', 'archivo_audio', 'html', 'pdf', 'activo']
    exclude = ('slug','autor', 'modificado', 'vistas',)
    ordering = ('categoria', 'orden_destacado', 'titulo', '-modificado',)
    search_fields = ('titulo','subtitulo')
    list_filter = ('modificado', 'orden_destacado', 'categoria')

    class Meta:
        model = Noticias

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
    #def save_model(self, request, obj, form, change):
    #    obj.autor = request.user
    #    obj.save()

"""
class VideoSMTAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url_video',)
    ordering = ('titulo', )

    class Meta:
        model = VideoSMT

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('descripcion','vision', 'justificacion', 'objetivos', 'usuarios')

    class Meta:
        model = Nosotros

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'ciudad', 'pais', 'modificado','textoMensage', )
    fields = ['nombre', 'email', 'telefono', 'ciudad', 'pais', 'textoMensage', 'modificado','activo']
    ordering = ('-modificado', 'nombre', )
    search_fields = ('modificado','nombre')

    class Meta:
        model = Contacto

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
"""

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Portada, PortadaAdmin)
admin.site.register(Reflexiones, ReflexionesAdmin)
#admin.site.register(SubCategoria, SubCategoriaAdmin)
admin.site.register(Noticias, NoticiasAdmin)
#admin.site.register(VideoSMT, VideoSMTAdmin)
#admin.site.register(Nosotros, NosotrosAdmin)
#admin.site.register(Contacto, ContactoAdmin)