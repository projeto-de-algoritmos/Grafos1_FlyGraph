
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import script


@api_view(['GET'])
def getData(request):

    origin = int(request.query_params['ido'])
    destination = int(request.query_params['idd'])
    result = script.bfsExecute(origin, destination)
    response = result.to_dict()
    # print(response)

    return Response(response)


@api_view(['GET'])
def getAirports(request):

    response = script.returnAirport()
    return Response(response)


@api_view(['GET'])
def checkGraph(request):

    response = script.checkGraph()
    return Response(response)
