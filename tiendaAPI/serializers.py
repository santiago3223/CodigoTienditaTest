from rest_framework import serializers

from tiendaAPI.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ["id", "descripcion"]