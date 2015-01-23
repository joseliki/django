from django.db import models
from django.contrib import admin
# Create your models here.
class Usuario(models.Model):
	cod = models.IntegerField(max_length=5)
	usuario = models.CharField(max_length=15)
	email = models.CharField(max_length=20)

class Libro(models.Model):
	cod = models.IntegerField(max_length=5)
	nombre = models.CharField(max_length=20)
	fecha_publicacion = models.DateField()
	Descripcion = models.CharField(max_length=30)
	categoria = models.CharField(max_length=20)
	
class Descarga(models.Model):
	cod = models.IntegerField(max_length=4)
	archivo = models.FileField(upload_to='.')	

class Comentario(models.Model):
	cod = models.IntegerField(max_length=5)
	comentario = models.CharField(max_length=200)
	fecha = models.DateTimeField()


admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Descarga)
admin.site.register(Comentario)
