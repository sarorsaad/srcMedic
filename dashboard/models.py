from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
 

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        pass
