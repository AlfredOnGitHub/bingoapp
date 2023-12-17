from django.db import models

class Juego(models.Model):
    numeros_dichos = models.JSONField(default=list, blank=True, null=True)