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