from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    rank = models.IntegerField()

    def __str__(self):
        return self.username
