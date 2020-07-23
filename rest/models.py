from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class DataModel(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    saving = models.TextField()

    def __str__(self):
        return self.player.username