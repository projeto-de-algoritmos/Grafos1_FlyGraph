from pandas import *
from graphs import *
from queue import Queue

if __name__ == "__main__":
    nodesList = []

    xls = ExcelFile("./data/data.xlsx")
    nodes = xls.parse(xls.sheet_names[0]).to_dict()
    edges = xls.parse(xls.sheet_names[1]).to_dict()

    criaNos(nodesList=nodesList, nodes=nodes)
    criaArestas(nodesList=nodesList, edges=edges)
    imprimeGrafo(nodesList=nodesList)

    # xls = ExcelFile("./data/pessoas.xlsx")
    # nodes = xls.parse(xls.sheet_names[0]).to_dict()
    # edges = xls.parse(xls.sheet_names[1]).to_dict()

    # criaNos(nodesList=nodesList, nodes=nodes)
    # criaArestas(nodesList=nodesList, edges=edges)
    # imprimeGrafo(nodesList=nodesList)


def bfs(source, end):
    visited = {}
    parent = {}
    queue = Queue()

    for node in nodesList:
        visited[node.id] = False
        parent[node.id] = None

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
                        print(u.id)
                        n= next((x for x in nodesList if x.id == v.f), None)
                        queue.put(n)

    path = []
    print(parent)
    if parent[end] != None:
        while end is not None:
            path.append(end)
            end = parent[end]
        path.reverse()
        print(path)
    else:
        print("Não existe caminho")

bfs("A", "C")
