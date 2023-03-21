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
    
class CreateArtista(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    anioNac = graphene.Int()
    edad = graphene.Int()
    generoArtist = graphene.String() 
    nacionalidad = graphene.String()
    generoMusica = graphene.String()
    cantIntegrantes = graphene.Int()
    cantAlbumes = graphene.Int() 
    cantSencillos = graphene.Int()
    cantTours = graphene.Int()

    #2 parametros que recibe la API
    class Arguments:
        id = graphene.Int()
        nombre = graphene.String()
        anioNac = graphene.Int()
        edad = graphene.Int()
        generoArtist = graphene.String() 
        nacionalidad = graphene.String()
        generoMusica = graphene.String()
        cantIntegrantes = graphene.Int()
        cantAlbumes = graphene.Int() 
        cantSencillos = graphene.Int()
        cantTours = graphene.Int()

    #3 
    def mutate(self, info, id, nombre, anioNac, edad, generoArtist, nacionalidad, generoMusica, 
               cantIntegrantes, cantAlbumes, cantSencillos, cantTours):
        artista = Artista(
                            id = id,
                            nombre=nombre, 
                            anioNac=anioNac, 
                            edad=edad, 
                            generoArtist=generoArtist, 
                            nacionalidad=nacionalidad, 
                            generoMusica=generoMusica, 
                            cantIntegrantes=cantIntegrantes, 
                            cantAlbumes=cantAlbumes, 
                            cantSencillos=cantSencillos, 
                            cantTours=cantTours
                            )
        artista.save()

        return CreateArtista(
            id=artista.id,
            nombre=artista.nombre,
            anioNac=artista.anioNac,
            edad=artista.edad, 
            generoArtist=artista.generoArtist, 
            nacionalidad=artista.nacionalidad, 
            generoMusica=artista.generoMusica, 
            cantIntegrantes=artista.cantIntegrantes, 
            cantAlbumes=artista.cantAlbumes, 
            cantSencillos=artista.cantSencillos, 
            cantTours=artista.cantTours
        )


#4
class Mutation(graphene.ObjectType):
    create_artista = CreateArtista.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)