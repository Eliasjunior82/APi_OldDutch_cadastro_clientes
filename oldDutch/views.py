from django.http import JsonResponse
from rest_framework import viewsets
from oldDutch.models import cliente
from oldDutch.serializers import ClienteSerializer


# Create your views here.
#def clientes (request):
 #   if request.method == 'GET':
  #      clientes = {'id': 1, 'nome': 'Junior', }
   #     return JsonResponse(clientes)
class ClientesViewset(viewsets.ModelViewSet):
    """"Exibe todos os clientes """
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer
