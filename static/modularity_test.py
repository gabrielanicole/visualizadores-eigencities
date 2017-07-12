import community as comu
import networkx as nx
import matplotlib.pyplot as plt

#import numpy as np
#from scipy import linalg, optimize
import datetime
from pymongo import MongoClient


#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
#G = nx.erdos_renyi_graph(30, 0.05)
def main():
	torres = ["PNCYA", "TSMAQ", "ANORO", "HBCAL", "VIAMU", "MMERF", "ANOMA", "POYAF", "SALAL"]

	G = loadNet(torres)

	print("G.edges()")
	print(G.edges())
	#first compute the best partition
	partition = comu.best_partition(G)
	print("partition")
	print(partition)

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
	
	print("red_array")
	print(red_array)

	for nodo in net_mongo:
		red_array.append((nodo["nodoi"],nodo["nodoj"],nodo["peso"]))
	
	net.add_weighted_edges_from(red_array)
	

	return net

if __name__ == '__main__':
	main()

