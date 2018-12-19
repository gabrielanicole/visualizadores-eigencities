import json
import math 
import numpy as np
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from escalamiento.models import Comuna_esc

import jsonpickle



#Create your views here.
def index(request):

	if request.method == 'POST':
		print("ENPOST ")
		if 'varSelect' in request.POST:
			print("Llamada desde cambio de variable")
			varSelect = request.POST['varSelect']
			logVar = "log_" + varSelect
			#if log: 
			data = list(Comuna_esc.objects.values_list("nombre", "log_pob_Comun_2002" , logVar, "pob_Comun_2002", varSelect, "lat", "lon", 'id' ))
			
			data_x = [float(x[1]) for x in data if  x[1] and x[2] and len(str(x[2])) > 3 ]
			data_y = [float(x[2]) for x in data if  x[1] and x[2] and len(str(x[2])) > 3 ]
			reg = np.polyfit(data_x, data_y , 1) 
			data = [ x for x in data if  x[1] and x[2] and len(str(x[2])) > 3 ]
			#data = dict(Comuna_esc.objects.values_list("nombre", "log_pob_Comun_2002" , varSelect ))
			print(reg)
			#If logaritmo: --> para implmentar en el futuro si no es simpre en log. 
			#data_log = [ (x[0], x[1], math.log(x[2]) ) for x in data if type(x[2]) != float  ]
			#print(data_log)
			print("enviado")
			return JsonResponse({'results': data, 'reg': list(reg) }, safe=False)


	ciudades = Comuna_esc.objects.all()
	#print(ciudades#)
	#for i in ciudades: 
	#	print(i.nombre, i.lat, i.lon)


	
	return render(request, 'escalamiento.html', {"ciudades": ciudades} )


def ciudad(request, pk):
	print("ciudad", pk)

	comuna = Comuna_esc.objects.filter(id= pk).values()
	#print(comuna[0])

	context = {}
	context['ciudades'] = jsonpickle.encode(comuna[0])
	print(context)

	return render(request, 'ciudad.html', context )
