from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()#(max_digits=3)
    direccion = models.CharField(max_length=255, default='Sin dirección')
    donador = models.BooleanField()
    
 