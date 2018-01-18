import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento
from django.core.serializers import serialize


# Create your views here.

def index(request):
	if request.method == 'POST':
		print("ENPOST ")
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