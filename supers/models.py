from django.db import models
from django.forms import CharField

from super_type.models import Super_Type

class Supers(models.Model):
    name = models.CharField(max_length=250)
    alter_ego = models.CharField(max_length=250)
    primary_ability= models.CharField(max_length=250)
    secondary_ability = models.CharField(max_length=250)
    catchphrase = models.CharField(max_length=250)
    super_type = models.ForeignKey(Super_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

