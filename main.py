from pandas import *
from djangoConfig.api.graphs import *
from djangoConfig.api.utils import *
from os import *

def clear():
    system('cls' if __name__ == 'nt' else 'clear')

if __name__ == "__main__":
    nodesList = []

    # AEROPORTOS
    xls = ExcelFile("./djangoConfig/api/data/aeroportos.xlsx")
    nodes = xls.parse(xls.sheet_names[0]).to_dict()
    xls = ExcelFile("./djangoConfig/api/data/tarifas.xlsx")
    edges = xls.parse(xls.sheet_names[0]).to_dict()

    createAirports(nodesList=nodesList, nodes=nodes)
    createFlights(nodesList=nodesList, edges=edges)

    clear()
    for i in range(len(nodesList)):
        print(f"({i+1}) => {nodesList[i].name} ({nodesList[i].state})")    
    print("Qual o (ID) do aeroporto que será sua origem?")
    origin = int(input())
    print("Qual o (ID) do aeroporto que será seu destino?")
    destination = int(input())

    finalPath = bfs(nodesList, nodesList[origin-1].oaci, nodesList[destination-1].oaci)
    names = []
    # if finalPath is not None:
    #     for airport in finalPath:
    #         names.append(airport.name)
    # print("RESULTADO DO MENOR CAMINHO:")
    # print("Não há caminho" if finalPath is None else names)

    i = 0
    totalPrice = 0
    for airport in finalPath:
        for flight in airport.flights:
            if i != len(finalPath)-1:
                if flight.used == True and flight.origin == finalPath[i].oaci and flight.destination == finalPath[i+1].oaci:
                    print(f".........................................................................\nPASSO {i+1} .............. Voo DE({flight.origin} - {finalPath[i].name}) => PARA({flight.destination} - {finalPath[i+1].name}) \n.....................: {flight.seats} Assentos disponíveis | Preço: R${flight.price}\n.........................................................................\n")
                    i += 1
                    totalPrice += flight.price
                    break
    print(f"PREÇO TOTAL DA VIAGEM: R${totalPrice}")

    # plotGraph(finalPath)
    # print(finalPath)
    # pprint(finalPath)