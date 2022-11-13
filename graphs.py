import sys
import copy

sys.path.insert(0, "models")
sys.path.insert(0, "data")

from queue import Queue
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


def bfs(nodesList, source, end):
    visited = {}
    parent = {}
    nodes = {}
    queue = Queue()

    for node in nodesList:
        visited[node.id] = False
        parent[node.id] = None
        nodes[node.id] = node

    # print(visited)
    # print(parent)
    # print(nodes)

    visited[source]= True
    n = next((x for x in nodesList if x.id == source), None)
    queue.put(n)

    for node in nodesList:
        if not visited[node.id]:           
            
            while not queue.empty():
                u = queue.get()
                for v in u.la:
                    if not visited[v.f]:
                        parent[v.f] = u.id
                        visited[v.f] = True
                        n = next((x for x in nodesList if x.id == v.f), None)
                        queue.put(n)

    path = []
    if parent[end] != None:
        while end is not None:
            path.append(copy.copy(nodes[end]))
            end = parent[end]
        path.reverse()
        return path