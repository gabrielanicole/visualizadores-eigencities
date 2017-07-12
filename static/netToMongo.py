#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Script para cargar datos de la red a MongoDB DB: EigenRedes
#coleccion redRanking --> {nodoi: "MUPAC", nodoj: "LECHE", peso: 50}
#coleccion nodos_ {nodoi: [coordenadas]}
#coleccion ranking y comunidades_ {nodoi: {nombre: "MUPAC ", coord: [coord], ranking: {id: 01, fecha: "ddmmaa", valor: 50 }, comunidad: {id: 01, fecha: "ddmmaa", ncom: 1 }} }

import json
import sys
import networkx
import numpy as np
from scipy import linalg, optimize
from pymongo import MongoClient
import datetime


def getNetworkFromPAJEK(filepath):
	return (networkx.read_pajek(filepath))

def main():

	client = MongoClient()
	db = client.EigenRedes
	coll = db.redRanking
	#print(coll.find())
	for document in coll.find():
		print(document)

	net = getNetworkFromPAJEK('03_16_v2.net')

	for nodo in net.edges(data='weight'):
		result = coll.insert_one({"nodoi" : nodo[0], "nodoj" : nodo[1], "peso": nodo[2]})
		print({"nodoi" : nodo[0], "nodoj" : nodo[1], "peso": nodo[2]})
	print(coll.find())
	print("listo")
	

if __name__ == '__main__':
	main()