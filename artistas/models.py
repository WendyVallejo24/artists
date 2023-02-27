from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.TextField(default='', blank= False)
    anioNac = models.IntegerField(default=0, blank= False)
    edad = models.PositiveSmallIntegerField(default=0)
    generoArtist = models.CharField(default='', max_length=1,blank= False) 
    nacionalidad = models.TextField(default='', blank= False)
    generoMusica = models.TextField(default='', blank= False)
    cantIntegrantes = models.PositiveSmallIntegerField(default=1)
    cantAlbumes = models.PositiveSmallIntegerField(default=0) 
    cantSencillos = models.PositiveSmallIntegerField(default=0)
    cantTours = models.PositiveSmallIntegerField(default=0)