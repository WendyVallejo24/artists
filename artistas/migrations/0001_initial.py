# Generated by Django 3.1.3 on 2023-02-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(default='')),
                ('anioNac', models.IntegerField(default=0)),
                ('edad', models.PositiveSmallIntegerField(default=0)),
                ('generoArtist', models.CharField(default='', max_length=1)),
                ('nacionalidad', models.TextField(default='')),
                ('generoMusica', models.TextField(default='')),
                ('cantIntegrantes', models.PositiveSmallIntegerField(default=1)),
                ('cantAlbumes', models.PositiveSmallIntegerField(default=0)),
                ('cantSencillos', models.PositiveSmallIntegerField(default=0)),
                ('cantTours', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
