from django.db import models


# Create your models here.
class BoatTeam(models.Model):
    name = models.CharField('name', max_length=100)

    class Meta:
        verbose_name = 'boat member'

    def __str__(self):
        return self.name



