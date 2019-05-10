from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización") 

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name 


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido") 
    published = models.DateTimeField(verbose_name="Fecha de publicación",  default=timezone.now()) 
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) 
    author = 
    categories = 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title


