from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50) 
    lat = models.DecimalField(max_digits=9, decimal_places=4)  
    lon = models.DecimalField(max_digits=9, decimal_places=4) 
    zoom = models.IntegerField()
    def __unicode__(self): # __unicode__ on Python 2
        return self.nombre

class Indicador(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    def __unicode__(self): # __unicode__ on Python 2
        return self.nombre
    
class CiudIndic(models.Model):
    residentesTotal = models.IntegerField() 
    movimientoTotal = models.IntegerField()
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE) 
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

class Antena(models.Model):
    nombre = models.CharField(max_length=50) 
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    lat = models.DecimalField(max_digits=9, decimal_places=4) 
    lon = models.DecimalField(max_digits=9, decimal_places=4)
    voronoi = models.CharField(max_length=200, blank= True)
    residentesTotal = models.IntegerField(blank= True, null = True)
    habitantesTotal = models.IntegerField(blank= True, null = True )
    def __unicode__(self): # __unicode__ on Python 2
        return self.nombre

class AntIndic(models.Model):
    #nombre = models.CharField(max_length=50) 
    antena = models.ForeignKey(Antena, on_delete=models.CASCADE) 
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE) 
    cantidad = models.DecimalField(max_digits=9, decimal_places=4) 

class Persona(models.Model):
    numa = models.CharField(max_length=50, unique = True) 
    residencia = models.ForeignKey(Antena, on_delete=models.CASCADE)

    def __unicode__(self): # __unicode__ on Python 2
        return self.numa

class Estadia(models.Model):
    numa = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    horaP = models.IntegerField()
    #horaf = models.IntegerField()
    dia = models.CharField(max_length=50)
    antena = models.ForeignKey(Antena, on_delete=models.CASCADE) 
    def __unicode__(self): # __unicode__ on Python 2
        return self.antena

    class Meta:
        unique_together = ('numa', 'horaP', 'dia', )
     

class Desplazamiento(models.Model):
    dia = models.CharField(max_length=50) 
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE) 
    hora = models.IntegerField()
    personasTotal = models.IntegerField() 
    movimientoTotal = models.IntegerField()
    suma = models.IntegerField()
    mediana = models.IntegerField()
    moda = models.IntegerField()
    promedio = models.IntegerField()
    desviacionSt = models.IntegerField()
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    varianza = models.IntegerField()
    p25 = models.IntegerField()
    p50 = models.IntegerField()
    p75 = models.IntegerField()
    
    def __unicode__(self): # __unicode__ on Python 2
        return self.hora


 
