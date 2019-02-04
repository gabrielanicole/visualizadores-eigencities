import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona

from django.core.serializers import serialize


from random import randint

# Create your views here.

def index(request):

	if request.method == 'POST':
		print("ENPOST ")

		if 'torreTray' in request.POST:
			print("antena en torreTray")
			nom_torre= request.POST['torreTray'] 
			diaAnalisis  = request.POST['diaAnalisis']
			numT  = request.POST['numT'][0]
			analisisTR = request.POST['analisisTR']
			numT = int(numT)
			antena = Antena.objects.filter(nombre = nom_torre)

			# print(antena[0])
			antena = antena[0]
			desplazamientosAntena = Estadia.objects.values('numa_id').distinct().filter(antena = antena, dia = diaAnalisis)
			
			def primero(user, antena):
				persona = Persona.objects.get(id = user['numa_id'])
				estadiasPersona = Estadia.objects.filter(numa = persona, dia = diaAnalisis).values_list('antena__lat', 'antena__lon', 'horaP', 'antena__nombre').order_by('horaP').first()

				if estadiasPersona[3] == antena.nombre:
					return True 
				else:
					return False  
			print("desplazamientosAntena")
			print(desplazamientosAntena)

			if analisisTR == "TR2":

				desplazamientosAntena = [user for user in desplazamientosAntena if primero(user, antena)]

			tray = []
			#numT usuarios al azar:
			usuarios_a=[]
			while (len(usuarios_a) < numT) and (len(usuarios_a) < len(desplazamientosAntena)):

				nuevo_indice = randint(0,len(desplazamientosAntena) -1 )
				if not (nuevo_indice in usuarios_a):
					usuarios_a.append(nuevo_indice)
					user = desplazamientosAntena[nuevo_indice]
					persona = Persona.objects.get(id = user['numa_id'])
					resd = persona.residencia
					indicadores = AntIndic.objects.filter(antena = resd).values_list('indicador__nombre', 'cantidad')
					estadiasPersona = Estadia.objects.filter(numa = persona, dia = diaAnalisis).values_list('antena__lat', 'antena__lon', 'horaP', 'antena__nombre').order_by('horaP')
					
					tray.append({ "numa":persona.numa, "moves": list(estadiasPersona), "NSE" : list(indicadores) })
			return JsonResponse({'results': tray}, safe=False)



			# for user in desplazamientosAntena:
			# 	print(user['numa_id'])
			# 	persona = Persona.objects.get(id = user['numa_id'])
			# 	resd = persona.residencia
			# 	indicadores = AntIndic.objects.filter(antena = resd).values_list('indicador__nombre', 'cantidad')
			# 	estadiasPersona = Estadia.objects.filter(numa = persona, dia = diaAnalisis).values_list('antena__lat', 'antena__lon', 'horaP', 'antena__nombre').order_by('horaP')
			# 	tray.append({ "numa":persona.numa, "moves": list(estadiasPersona), "NSE" : list(indicadores) })
			# return JsonResponse({'results': tray}, safe=False)
    	
    	if 'cidadTorres' in request.POST:
    		id_ciudadPOST= request.POST['cidadTorres'] 
    		antenas = Antena.objects.filter(ciudad = id_ciudadPOST)
    		antenasIndicadores = AntIndic.objects.filter(antena__in = antenas ).values('antena','indicador__nombre','cantidad')
    		print(antenasIndicadores)
    		return JsonResponse({'results': list(antenas.values()), 'antIndic': list(antenasIndicadores) }, safe=False)
    	
    	if 'analisis' in request.POST:
			tipo_analisis  = request.POST['analisis']
			ciudadAn  = request.POST['ciudadAnalisis']
			indicadores  = request.POST['indicadoresAnalisis']
			diaAnalisis  = request.POST['diaAnalisis']
			indicadores = json.loads(indicadores)
			#indicadores = map(int, indicadores)
			print(indicadores)
			if tipo_analisis == "DT" or tipo_analisis == "DH":
				indicadoresCiudad = CiudIndic.objects.filter(ciudad = ciudadAn).values()
				desplazamiento = Desplazamiento.objects.filter(ciudad = ciudadAn, indicador__in = indicadores, dia = diaAnalisis).values(
					'dia','ciudad__nombre','indicador','indicador__nombre','hora','personasTotal','movimientoTotal','suma','mediana','moda','promedio','desviacionSt','minimo','maximo','varianza','p25','p50','p75',) 
				return JsonResponse({'results': list(desplazamiento)}, safe=False)
			else:
				return JsonResponse({'results': list([])}, safe=False)



	ciudades = Ciudad.objects.all()
	print(ciudades)
	indicadores = Indicador.objects.all()

	return render(request, 'tray.html', {"ciudades": ciudades, "indicadores": indicadores})