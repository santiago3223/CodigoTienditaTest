from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from tiendaAPI.models import Categoria
from tiendaAPI.serializers import CategoriaSerializer


class CategoriaList(generics.ListAPIView):


    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

