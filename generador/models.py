from django.db import models

# Create your models here.

class Token(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    token = models.CharField(max_length=7)