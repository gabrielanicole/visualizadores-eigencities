import json
import math 
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from escalamiento.models import Comuna_esc

#Create your views here.
def index(request):

	if request.method == 'POST':
		print("ENPOST ")
		if 'varSelect' in request.POST:
			print("Llamada desde cambio de variable")
			varSelect = request.POST['varSelect']
			#if log: 
			data = list(Comuna_esc.objects.values_list("nombre", "log_pob_Comun_2002" , varSelect ))
			
			#If logaritmo: --> para implmentar en el futuro si no es simpre en log. 
			#data_log = [ (x[0], x[1], math.log(x[2]) ) for x in data if type(x[2]) != float  ]
			#print(data_log)
			print("enviado")
			return JsonResponse({'results': data }, safe=False)


	ciudades = Comuna_esc.objects.all()
	#print(ciudades#)
	#for i in ciudades: 
	#	print(i.nombre, i.lat, i.lon)


	
	return render(request, 'escalamiento.html', {"ciudades": ciudades} )
