from pyexpat import model
from django.db import models

# Create your models here.
class cliente (models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    data = models.DateField(max_length= 8)


    def __str__(self):
        return self.nome