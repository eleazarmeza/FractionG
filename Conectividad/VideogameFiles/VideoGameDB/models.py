from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    puntaje = models.PositiveIntegerField()
    def __str__(self):
        return self.name


class Players(models.Model):
    Grupo = models.PositiveIntegerField()
    Numero_de_Lista = models.PositiveIntegerField()
    Password = models.CharField(max_length=50)

