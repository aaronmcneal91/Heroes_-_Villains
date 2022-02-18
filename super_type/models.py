from django.db import models
# from supers import Super

class Super_Type(models.Model):
    type = models.CharField(max_length=7)
     
    def __str__(self):
        return self.type

