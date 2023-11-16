from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.

class ClaseModelo(models.Model):
    activo = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Categoria(ClaseModelo):
    nombre = models.CharField(max_length=100, help_text='Categoría', unique=True)
    imagen = models.FileField("Imagen categoria", upload_to="imagenes/categorias",default="")

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorías"

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, help_text='Descripción de la sub categoría')
    imagen = models.FileField("Imagen categoria", upload_to="imagenes/categorias",default="")

    def __str__(self):
        return '{}: {}'.format(self.categoria.nombre,self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','nombre')

class Portada(ClaseModelo):
    nombre = models.CharField(max_length=100, help_text='Nombre')
    imagen = models.FileField("Imagen Portada (1920 x 947 px)", upload_to="imagenes/portada",default="")

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Portada, self).save()

    class Meta:
        verbose_name_plural = "Portada"
        unique_together = ('nombre',)

class Reflexiones(ClaseModelo):
    nombre = models.CharField(max_length=100, help_text='Nombre')
    fecha = models.DateField('Fecha', blank=True, null=True, default=datetime.now)
    url_video = models.CharField("Video", max_length=1000, default="")
    foto = models.FileField("Imagen Destacado (400 x 400 px)", upload_to="imagenes/reflexiones/", blank=False, null=False, default='')

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Reflexiones, self).save()

    class Meta:
        verbose_name_plural = "Reflexiones"
        unique_together = ('nombre','url_video')

class Suscribir(ClaseModelo):
    email = models.CharField(max_length=200, help_text='eMail', unique=True)

    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        verbose_name_plural = "Suscribirse"

class Nosotros(ClaseModelo):
    descripcion = RichTextField(max_length=10000, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.idEmisora)

    def save(self):
        super(Nosotros, self).save()

    class Meta:
        verbose_name_plural = "Nosotros"


class VideoFaceBook(ClaseModelo):
    titulo = models.CharField(blank=False, null=False, max_length=200)
    url_video = models.TextField("ingrese la URL del vídeo.",max_length=250, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper()
        super(VideoFaceBook, self).save()

    class Meta:
        verbose_name_plural = "Videos FaceBookLive"

class Contacto(ClaseModelo):
    nombre = models.CharField(help_text='Nombre y Apellidos', blank=False, null=False, max_length=200)
    email = models.CharField(help_text='Correo electrónico', blank=False, null=False, max_length=200)
    telefono = models.CharField(help_text='Teléfono de contacto', blank=True, null=True, max_length=100, default="")
    ciudad = models.CharField(help_text='Ciudad de residencia', blank=True, null=True, max_length=100, default="")
    pais = models.CharField(help_text='País de residencia', blank=True, null=True, max_length=100, default="")
    textoMensage = models.TextField(help_text='Mensage', blank=False, null=False, max_length=10000)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        self.nombre = self.ciudad.upper()
        self.nombre = self.pais.upper()
        super(Contacto, self).save()

    class Meta:
        verbose_name_plural = "Contactos"

class Noticias(ClaseModelo):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0, null=False, blank=False)
    titulo = models.CharField(help_text='Título de la noticia', blank=False, null=False, max_length=200)
    subtitulo = models.CharField(help_text='Sub título de la noticia', blank=False, null=False, max_length=500)
    descripcion = RichTextField(max_length=15000, blank=True, null=True)
    archivo_audio = models.FileField("Archivo Audio", upload_to="audio/", blank=True, null=True, default='')
    fecha_inicio_publicacion = models.DateField('Fecha de inicio de publicación', blank=True, null=True, default=datetime.now)
    fecha_final_publicacion = models.DateField('Fecha de finalización de publicación', blank=True, null=True, default=datetime.now)
    CHOICES = ((0,'Titulares'),(1,'Destacado 1'),(2,'Destacado 2'),(3,'General'))
    orden_destacado = models.IntegerField(choices=CHOICES, default=0, blank=False, null=False)
    imagen_destacado = models.FileField("Imagen Destacado (915 x 770 px)", upload_to="imagenes/", blank=False, null=False)
    html = models.TextField(max_length=10000, default="", blank=True, null=True)
    pdf = models.FileField("Archivo PDF", upload_to="pdf/", blank=True, null=True, default='')
    slug = models.SlugField(blank=True,null=True, max_length=250)
    
    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.slug = slugify(self.titulo)
        super(Noticias, self).save()

    class Meta:
        verbose_name_plural = "Noticias"

class Comentario(ClaseModelo):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, default=0, null=False, blank=False)
    comentario = models.TextField(max_length=10000, blank=True, null=True)
    nombre = models.CharField(blank=False, null=False, max_length=200)
    email = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = "Comentarios"

