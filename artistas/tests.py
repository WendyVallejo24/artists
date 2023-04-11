from django.test import TestCase

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from artistas.schema import schema
from artistas.models import Artista

ARTISTAS_QUERY = '''
 { artistas { id nombre anioNac edad generoArtist nacionalidad generoMusica cantIntegrantes cantAlbumes cantSencillos cantTours }}
'''
CREATE_ARTISTAS_MUTATION = '''
mutation createArtistaMutation($id: Int, $nombre: String, $anioNac: Int, $edad: Int, $generoArtist: String, $nacionalidad: String, $generoMusica: String, $cantIntegrantes: Int, $cantAlbumes: Int, $cantSencillos: Int, $cantTours: Int) { 
 createArtista(id: $id, nombre: $nombre, anioNac: $anioNac, edad: $edad, generoArtist: $generoArtist, nacionalidad: $nacionalidad, generoMusica: $generoMusica, cantIntegrantes: $cantIntegrantes, cantAlbumes: $cantAlbumes, cantSencillos: $cantSencillos, cantTours: $cantTours) { 
  nombre
 }
}
'''

class ArtistaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.artista1 = mixer.blend(Artista)
        self.artista2 = mixer.blend(Artista)

    def test_artistas_query(self):
        response = self.query(
            ARTISTAS_QUERY,
        )

        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print ("query artistas results ")
        print (content)
        assert len(content['data']['artistas']) == 2

    def test_createArtista_mutation(self):
        response = self.query(
            CREATE_ARTISTAS_MUTATION,
            variables={'id': 6, 'nombre': 'Sebastian Yatra', 'anioNac': 1994, 'edad': 28, 'generoArtist': 'M', 'nacionalidad': 'Colombiana', 'generoMusica': 'pop', 'cantIntegrantes': 1, 'cantAlbumes': 4, 'cantSencillos': 40, 'cantTours': 3}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createArtista": {"nombre": "Sebastian Yatra"}}, content['data'])