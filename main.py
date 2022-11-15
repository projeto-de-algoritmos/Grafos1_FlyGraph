from pandas import *
from graphs import *
from utils import *
from os import *

def clear():
    system('cls' if __name__ == 'nt' else 'clear')

if __name__ == "__main__":
    nodesList = []

    # ABCDEFJHIJ
    # xls = ExcelFile("./data/data.xlsx")
    # nodes = xls.parse(xls.sheet_names[0]).to_dict()
    # edges = xls.parse(xls.sheet_names[1]).to_dict()

    # criaNos(nodesList=nodesList, nodes=nodes)
    # criaArestas(nodesList=nodesList, edges=edges)
    # imprimeGrafo(nodesList=nodesList)

    # PESSOAS 
    # xls = ExcelFile("./data/pessoas.xlsx")
    # nodes = xls.parse(xls.sheet_names[0]).to_dict()
    # edges = xls.parse(xls.sheet_names[1]).to_dict()

    # criaNos(nodesList=nodesList, nodes=nodes)
    # criaArestas(nodesList=nodesList, edges=edges)
    # imprimeGrafo(nodesList=nodesList)

    # AEROPORTOS
    xls = ExcelFile("./data/aeroportos.xlsx")
    nodes = xls.parse(xls.sheet_names[0]).to_dict()
    xls = ExcelFile("./data/tarifas.xlsx")
    edges = xls.parse(xls.sheet_names[0]).to_dict()

    criaNos(nodesList=nodesList, nodes=nodes)
    criaArestas(nodesList=nodesList, edges=edges)
    # imprimeGrafo(nodesList=nodesList)

    clear()
    for i in range(len(nodesList)):
        print(f"({i+1}) => {nodesList[i].name}")    
    print("Qual o (ID) do aeroporto que será sua origem?")
    origin = int(input())
    print("Qual o (ID) do aeroporto que será seu destino?")
    destination = int(input())

    fp = bfs(nodesList, nodesList[origin-1].id, nodesList[destination-1].id)
    names = []
    if fp is not None:
        for person in fp:
            names.append(person.name)
    print("RESULTADO DO MENOR CAMINHO:")
    print("Não há caminho" if fp is None else names)

    # pprint(fp)