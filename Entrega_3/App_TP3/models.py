from django.db import models

# Create your models here.

class Camiseta(models.Model):
    equipo = models.CharField(max_length=30)
    año = models.IntegerField()
    equipación = models.CharField(max_length= 10)
    talle = models.CharField(max_length=4)

    def __str__(self):
        return f"Equipo: {self.equipo} - Año: {self.año} - Equipación: {self.equipación}"

class Pantalon(models.Model):
    equipo = models.CharField(max_length=30)
    año = models.IntegerField()
    equipación = models.CharField(max_length= 10)
    modelo = models.CharField(max_length=10)
    talle = models.CharField(max_length=4)  
    precio = models.IntegerField()

    def __str__(self):
        return f"Equipo: {self.equipo} - Año: {self.año} - Equipación: {self.equipación}"  

class Abrigo(models.Model):
    equipo = models.CharField(max_length=30)
    año = models.IntegerField()
    modelo = models.CharField(max_length=15)
    talle = models.CharField(max_length=4)

    def __str__(self):
        return f"Equipo: {self.equipo} - Año: {self.año} - Modelo: {self.modelo}"