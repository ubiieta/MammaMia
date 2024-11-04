from django.db import models

# Modelos para masas, ingredientes y pizzas

 
class Masa(models.Model):
    nombre = models.CharField(max_length=50)
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
 
class Pizza(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    
    # Campo para la relación one-to-many (una pizza tiene solo una masa)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (una pizza tiene varios ingredientes)
    ingredientes = models.ManyToManyField(Ingrediente)
    
   