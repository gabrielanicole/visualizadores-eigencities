import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona
from django.core.serializers import serialize


# Create your views here.

def index(request):
	if request.method == 'POST':
		print("ENPOST ")
		if 'torreTray' in request.POST:
			print("antena en torreTray")
			nom_torre= request.POST['torreTray'] 
			diaAnalisis  = request.POST['diaAnalisis']

			antena = Antena.objects.filter(nombre = nom_torre)
			# print(antena[0])
			antena = antena[0]
			desplazamientosAntena = Estadia.objects.values('numa_id').distinct().filter(antena = antena, dia = diaAnalisis)

			# print(desplazamientosAntena)
			tray = []
			for user in desplazamientosAntena:
				print(user['numa_id'])
				persona = Persona.objects.get(id = user['numa_id'])
				resd = persona.residencia
				indicadores = AntIndic.objects.filter(antena = resd).values('indicador__nombre', 'cantidad')
				print("indicadores")
				print(indicadores)
				# mydict.keys()[mydict.values().index(16)]
				ABC1 = [x['cantidad'] for x in indicadores if x['indicador__nombre'] == 'ABC1']
				print(ABC1)
				nse = {"ABC1": 0, "C2":0 , "C3": 0, "D": 0, "E": 0}
				for key in nse:
					print(key)
					ind = [x['cantidad'] for x in indicadores if x['indicador__nombre'] == key]
					nse[key] = ind[0] if len(ind) == 1 else 0 
				print("nse")
				print(nse)

				
				estadiasPersona = Estadia.objects.filter(numa = persona, dia = diaAnalisis).values_list('antena__lat', 'antena__lon', 'horaP',).order_by('horaP')
				# print("estadiasPersona")
				# print(list(estadiasPersona))
				tray.append({ "numa":persona.numa, "moves": list(estadiasPersona), "NSE" : nse })
 
			# print(tray)
			return JsonResponse({'results': tray}, safe=False)

		if 'cidadTorres' in request.POST:
			id_ciudadPOST= request.POST['cidadTorres'] 
			antenas = Antena.objects.filter(ciudad = id_ciudadPOST)
			antenasIndicadores = AntIndic.objects.filter(antena__in = antenas ).values(
				'antena','indicador__nombre','cantidad')

			print(antenasIndicadores)
			#antenas = json.dumps(antenas) 
			return JsonResponse({'results': list(antenas.values()), 'antIndic': list(antenasIndicadores) }, safe=False)
			#return JsonResponse(antenas, safe=False)
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