from pandas import *
from graphs import *

if __name__ == "__main__":
	nodesList = []

	xls = ExcelFile("./data/data.xlsx")
	nodes = xls.parse(xls.sheet_names[0]).to_dict()
	edges = xls.parse(xls.sheet_names[1]).to_dict()

	criaNos(nodesList=nodesList, nodes=nodes)
	criaArestas(nodesList=nodesList, edges=edges)
	imprimeGrafo(nodesList=nodesList)

	xls = ExcelFile("./data/pessoas.xlsx")
	nodes = xls.parse(xls.sheet_names[0]).to_dict()
	edges = xls.parse(xls.sheet_names[1]).to_dict()

	criaNos(nodesList=nodesList, nodes=nodes)
	criaArestas(nodesList=nodesList, edges=edges)
	imprimeGrafo(nodesList=nodesList)