import sys
import copy
from unittest import result
import networkx as nx
from queue import Queue
from .models.flight import Flight
from .models.airport import Airport

import matplotlib.pyplot as plt

sys.path.insert(0, "models")
sys.path.insert(0, "data")


def createAirports(nodesList, nodes):
    for i in nodes["OACI"]:
        airport = Airport(
            oaci=nodes["OACI"][i],
            state=nodes["UF"][i],
            operation=nodes["Operacao"][i],
            latitude=nodes["Latitude"][i],
            longitude=nodes["Longitude"][i],
            altitude=nodes["Altitude"][i],
            name=nodes["Nome"][i],
            town=nodes["Municipio_Atendido"][i],
            flights=[]
        )
        nodesList.append(airport)


def createFlights(nodesList, edges):
    airportNodes = {}
    for airport in nodesList:
        airportNodes[airport.oaci] = airport
    for i in edges["ORIGEM"]:
        flight = Flight(
            origin=airportNodes[edges["ORIGEM"][i]],
            destination=airportNodes[edges["DESTINO"][i]],
            price=edges["TARIFA"][i],
            seats=edges["ASSENTOS"][i],
            used=False
        )
        for node in nodesList:
            if edges["ORIGEM"][i] == node.oaci:
                node.appendEdge(flight)
                break


def printGraph(nodesList):
    for node in nodesList:
        edgeList = ''
        for edge in node.flights:
            edgeList = edgeList + edge.destination.oaci + ' '
        print(f"Nó({node.oaci}) -> LA: [ {edgeList}]")


def returnAirports(nodeList):
    result = []
    for node in nodeList:
        result.append(node.to_dict())
    print(len(result))
    return result


def bfs(nodesList, source, end):
    queue = Queue()
    visited = {}
    parent = {}
    nodes = {}

    for node in nodesList:
        visited[node.oaci] = False
        parent[node.oaci] = None
        nodes[node.oaci] = node

    visited[source] = True
    n = next((n for n in nodesList if n.oaci == source), None)
    queue.put(n)

    for node in nodesList:
        if not visited[node.oaci]:

            while not queue.empty():
                u = queue.get()
                for v in u.flights:
                    if not visited[v.destination.oaci]:
                        parent[v.destination.oaci] = u.oaci
                        v.used = True
                        visited[v.destination.oaci] = True
                        n = next(
                            (x for x in nodesList if x.oaci == v.destination.oaci), None)
                        queue.put(n)

    path = []
    if parent[end] != None:
        while end is not None:
            path.append(copy.copy(nodes[end]))
            end = parent[end]
        path.reverse()
        return path


def plotGraph(nodesList):
    G = nx.Graph()
    G.add_node(node.oaci for node in nodesList)
    for node in nodesList:
        for edge in node.flights:
            G.add_edge(edge.origin, edge.destination)
    nx.draw_networkx(G)
    plt.show()
