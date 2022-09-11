from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    rank = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    avatar = models.ImageField(default='')

    def __str__(self):
        return self.username
