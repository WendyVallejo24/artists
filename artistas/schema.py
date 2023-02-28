import graphene
from graphene_django import DjangoObjectType

from .models import Artista


class ArtistaType(DjangoObjectType):
    class Meta:
        model = Artista


class Query(graphene.ObjectType):
    artistas = graphene.List(ArtistaType)

    def resolve_artistas(self, info, **kwargs):
        return Artista.objects.all()