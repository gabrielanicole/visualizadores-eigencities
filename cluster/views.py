import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import sys
import networkx as nx
import numpy as np
from scipy import linalg, optimize
import datetime
from pymongo import MongoClient
import community as comu



import logging

VERIFIER = None

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     filename='/var/www/html/visualizador/visualizador_opencensus/django/cluster.log',
#                     #filename='cluster.log',
#                     filemode='w')
# logging.debug('A debug message')
# logging.info('Some information')
# logging.warning('A problem happened')
net = nx.Graph()
# Create your views here.
def index(request):
	#print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
	if request.method == 'POST':
		resp = ""

		if 'input' in request.POST:
			entrada = request.POST['input'] 
			resp = { 'salida': entrada}
			

		elif 'torres' in request.POST:
			
			torres = request.POST['torres']
			algoritmo = request.POST['algoritmo'] 

			# lista de torres seleccionadas
			l_torres = torres.split(",")
			print(l_torres)
			
			net = loadNet(l_torres)
			if (algoritmo == "rectangle"):
				eigenArray = saveEigenValues(net)
				
				print("eigenArray")
				print(eigenArray)

				salida = eigenArray.tolist()

			else:
				salida = comu.best_partition(net)
				


			resp = { 'salida': salida}
			
		elif 'inicio_red' in request.POST:
			# logging.debug('inicio_red')
			resp = loadNet(request)
			# logging.debug('red_cargada')
		
		return JsonResponse(resp, safe=False)

	
	return render(request, 'cluster.html')


def getNetworkFromPAJEK(filepath):
	return (nx.read_pajek(filepath))

def saveEigenValues(net):
	mat = nx.to_numpy_matrix(net)
	tower_dict = net.nodes(True)

	tower_dict = zip(*tower_dict)[0]
    
	# aplicamos eigen-algorithnRun eigh-algorithm
	vals, vecs = linalg.eigh(mat)
    
	# se considera el eigenvector con el mayor eigenvalue
	indexOfMax = np.where(vals == max(vals))[0][0]
	first_eigenvector = vecs[:, indexOfMax]
    
	# se realiza join del eigenvector con node_ids y se ordenan
	eigenvector_pair = zip(first_eigenvector, tower_dict)
	eigenvector_pair.sort(key=lambda x: x[0], reverse=True)
    
	# separamos pares en dos columnas
	columns = zip(*eigenvector_pair)
	columns[1] = map(lambda x: str(x), columns[1]) # transformamos a string
    
	# guardar ranking como archivo
	#np.savetxt( "RANKING_03_16_v2.txt", np.asarray([columns[0], columns[1]]).T, fmt="%s")
	

	# obtener ranking y graficar en interfaz
	return np.asarray([columns[0], columns[1]]).T # retorna los datos como array

def loadNet(l_torres):
	#global net 
	net=nx.Graph()

	client = MongoClient()
	db = client.django_example
	coll = db.redRanking
	net_mongo = coll.find(
		{
		"nodoi": { '$in': l_torres},
		"nodoj": { '$in': l_torres}
		}
		)

	net.add_nodes_from(l_torres)
	red_array = []
	

	for enlace in net_mongo:
		#net.add_weighted_edges_from([(enlace["nodoi"],enlace["nodoj"],enlace["peso"])])
		red_array.append((enlace["nodoi"],enlace["nodoj"],enlace["peso"]))
	net.add_weighted_edges_from(red_array)

	return net

