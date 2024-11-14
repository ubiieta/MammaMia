from django.db import models

# Modelos para masas, ingredientes y pizzas

 
class Masa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_extra = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    es_vegetariano = models.BooleanField(default=True)
    precio_extra = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre
 
class Pizza(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    tiempo_preparacion = models.IntegerField(default=15)
    imagen_url = models.URLField(blank=True, null=True)

    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    
    def __str__(self):
        return self.nombre
   