import sys
sys.path.insert(0, "models")
sys.path.insert(0, "data")

from edge import Aresta
from node import No

def criaNos(nodesList, nodes):
	for i in nodes["nós"]:
		node = No(id=nodes["nós"][i])
		nodesList.append(node)

def criaArestas(nodesList, edges):
	for i in edges["nó início"]:
		iN = edges["nó início"][i]
		fN = edges["nó fim"][i]
		edge = Aresta(i=iN, f=fN)
		for node in nodesList:
			if edges["nó início"][i] == node.id:
				node.appendEdge(edge)
				break

def imprimeGrafo(nodesList):
	for node in nodesList:
		edgeList = ''
		for edge in node.la:
			edgeList = edgeList + edge.f + ' '
		print(f"Nó({node.id}) -> LA: [ {edgeList}]")