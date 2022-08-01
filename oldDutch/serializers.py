from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from oldDutch.models import cliente

class ClienteSerializer(serializers.ModelSerializer):
    class meta:
        model = cliente
        field = ['id', 'nome','telefone', 'data' ]
        