import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento
from django.core.serializers import serialize


# Create your views here.

def index(request):
	ciudades = Ciudad.objects.all()
	print(ciudades)
	indicadores = Indicador.objects.all()

	return render(request, 'tray.html', {"ciudades": ciudades, "indicadores": indicadores})