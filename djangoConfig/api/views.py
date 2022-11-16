
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import script
import asyncio

@api_view(['GET'])
def getData(request):
    
    person= {"name": "Joao", "age:": 21}
    aa= script.bfsExecute(5,9)
    return Response(aa)
   


