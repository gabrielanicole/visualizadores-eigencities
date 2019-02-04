from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Conurbacion_esc(models.Model):
	nombre = models.CharField(max_length=50) 
	lat = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  
	lon = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True) 
	zoom = models.IntegerField(default=10)
	pob_Conurb_2002 = models.IntegerField(default=10)
	def __unicode__(self): # __unicode__ on Python 2
	    return self.nombre
	

class Variable(models.Model):
	nombre = models.CharField(max_length=50)
	nombre_mostrar = models.CharField(max_length=50, blank= True, null = True)  
	descripcion = models.CharField(max_length=5000, blank= True, null = True)
	medida = models.CharField(max_length = 100, blank= True, null = True)  
	fuente =models.CharField(max_length = 500, blank= True, null = True)  
	toma_dato = models.CharField(max_length = 100, blank= True, null = True)  
	regimen = models.CharField(max_length = 100, blank= True, null = True)
	a0b10 = models.DecimalField(max_digits=10, decimal_places=5, blank= True, null = True)  #(private transport, )
	mb10 = models.DecimalField(max_digits=10, decimal_places=5, blank= True, null = True)  #(private transport, )
	n_calculob10 = models.DecimalField(max_digits=10, decimal_places=5, blank= True, null = True)  #(private transport, )
	def __unicode__(self): # __unicode__ on Python 2
	    return self.nombre


class Comuna_esc(models.Model):
	nombre = models.CharField(max_length=50)  
	conurbacion = models.ForeignKey(Conurbacion_esc, on_delete=models.SET_NULL, blank= True, null = True)
	lat = models.DecimalField(max_digits=35,decimal_places=20, blank= True, null = True)  
	lon = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True) 
	zoom = models.IntegerField(default=10)
	pob_Comun_2002 = models.IntegerField(default=10)
	vehicle = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(vehicle, )
	motor = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(motor vehicle, )
	Non_motorized = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Non-motorized vehicle, )
	private_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(private transport, )
	public_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(public transport, )
	CO2_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(CO2(movil transport sources), )
	Green = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Green spaces , )
	Iliteracy = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Iliteracy, )
	Municipal_spending = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending(M$/hab), )
	Unemployment = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Unemployment, )
	Crime = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Crime reports, )
	Arrested = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Arrested person, )
	Companies = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Companies, )
	Sales = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Sales, )
	workers = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(workers, )
	Income = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Income(workers), )
	technicians = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Professional technicians, )
	University = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(University Professional, )
	Professionals = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Professionals, )
	Solid_waste = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Solid Waste, )
	Municipal_Power = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending for Power Consumption, )
	Municipal_Water = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending for Water Consumption, )
	Municipal_cleaning = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal Spending cleaning services + garbage collection + landfill, )
	Deaths = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Deaths, )
	Birthrate = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Birthrate, )
	Year_scholarship = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Year of scholarship, )
	Offence_Property = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Offence Against Property, )
	Offence_Person = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Offence Against the Person, )
	Burglary = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Burglary, )
	Robbery = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Robbery, )
	Injuries = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Injuries, )
	Indigenous = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Indigenous, )
	Emergency = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Emergency attendence, )
	Respiratory = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Respiratory Diseases, )
	Cardiovascular = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Cardiovascular Diseases, )
	Hospitalizations = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Hospitalizations, )
	Street = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Street length )

	log_pob_Comun_2002 = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(vehicle, )
	log_vehicle = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(vehicle, )
	log_motor = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(motor vehicle, )
	log_Non_motorized = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Non-motorized vehicle, )
	log_private_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(private transport, )
	log_public_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(public transport, )
	log_CO2_transport = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(CO2(movil transport sources), )
	log_Green = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Green spaces , )
	log_Iliteracy = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Iliteracy, )
	log_Municipal_spending = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending(M$/hab), )
	log_Unemployment = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Unemployment, )
	log_Crime = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Crime reports, )
	log_Arrested = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Arrested person, )
	log_Companies = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Companies, )
	log_Sales = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Sales, )
	log_workers = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(workers, )
	log_Income = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Income(workers), )
	log_technicians = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Professional technicians, )
	log_University = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(University Professional, )
	log_Professionals = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Professionals, )
	log_Solid_waste = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Solid Waste, )
	log_Municipal_Power = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending for Power Consumption, )
	log_Municipal_Water = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal spending for Water Consumption, )
	log_Municipal_cleaning = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Municipal Spending cleaning services + garbage collection + landfill, )
	log_Deaths = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Deaths, )
	log_Birthrate = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Birthrate, )
	log_Year_scholarship = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Year of scholarship, )
	log_Offence_Property = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Offence Against Property, )
	log_Offence_Person = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Offence Against the Person, )
	log_Burglary = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Burglary, )
	log_Robbery = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Robbery, )
	log_Injuries = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Injuries, )
	log_Indigenous = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Indigenous, )
	log_Emergency = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Emergency attendence, )
	log_Respiratory = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Respiratory Diseases, )
	log_Cardiovascular = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Cardiovascular Diseases, )
	log_Hospitalizations = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Hospitalizations, )
	log_Street = models.DecimalField(max_digits=35, decimal_places=20, blank= True, null = True)  #(Street length )



	def __unicode__(self): # __unicode__ on Python 2
	    return self.nombre




