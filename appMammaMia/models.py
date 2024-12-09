from django.db import models

# Modelos para masas, ingredientes y pizzas

 
class Masa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_extra = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Imagen')

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    es_vegetariano = models.BooleanField(default=True)
    precio_extra = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Imagen')

    def __str__(self):
        return self.nombre
 
class Pizza(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    tiempo_preparacion = models.IntegerField(default=15)
    imagen = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Imagen')

    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    
    def __str__(self):
        return self.nombre
    

class Reserva(models.Model):
    npersonas = models.PositiveIntegerField()
    hora = models.TimeField()
    fecha = models.DateField()
    email = models.EmailField()
   
    def __str__(self):
        return f"Reserva para {self.npersonas} personas el {self.fecha} a las {self.hora}"
